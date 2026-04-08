from django.db import models
import uuid

class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="事件標題")
    description = models.TextField(blank=True, verbose_name="事件描述")
    passcode = models.CharField(max_length=20, unique=True, verbose_name="委員進入碼")
    is_anonymous_results = models.BooleanField(default=False, verbose_name="結果匿名顯示")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "事件"
        verbose_name_plural = "事件"

class ScoringItem(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=100, verbose_name="項目名稱")
    weight = models.IntegerField(verbose_name="權重(%)")

    def __str__(self):
        return f"{self.name} ({self.weight}%)"

class Team(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="teams")
    name = models.CharField(max_length=100, verbose_name="組別名稱")

    def __str__(self):
        return self.name

class Commissioner(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="commissioners")
    name = models.CharField(max_length=100, verbose_name="委員姓名")
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name

class ScoreRecord(models.Model):
    commissioner = models.ForeignKey(Commissioner, on_delete=models.CASCADE, related_name="scores")
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    item = models.ForeignKey(ScoringItem, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="分數")

    class Meta:
        unique_together = ('commissioner', 'team', 'item')

class TeamRankRecord(models.Model):
    commissioner = models.ForeignKey(Commissioner, on_delete=models.CASCADE, related_name="ranks")
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    rank = models.IntegerField(verbose_name="序位")

    class Meta:
        unique_together = ('commissioner', 'team')
