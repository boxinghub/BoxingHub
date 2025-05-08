from django.db import models
from django.core.validators import MaxValueValidator



def metric_to_imperial(cm: float) -> str:
    """
    Convert a height in centimeters to feet and inches.
    """
    # Convert cm to total inches
    total_inches = cm / 2.54
    # Calculate whole feet
    feet = int(total_inches // 12)
    # Calculate remaining inches (rounded)
    inches = int(round(total_inches - (feet * 12)))
    return f"{feet}′ {inches}″"


def format_reach_imperial(cm: float) -> str:
    """
    Given a reach in cm, return a formatted string like "78″".
    """
    total_inches = cm / 2.54
    inches = int(round(total_inches))
    return f"{inches}″"


class Boxer(models.Model):
    first_name        = models.CharField(max_length=50)
    last_name         = models.CharField(max_length=50)
    sex               = models.CharField(max_length=1)
    alias             = models.CharField(max_length=50, blank=True, null=True)
    age               = models.PositiveSmallIntegerField()
    nationality       = models.CharField(max_length=50)
    stance            = models.CharField(max_length=20)
    
    # Metric measurements
    height_metric = models.IntegerField(validators=[MaxValueValidator(999)])
    reach_metric  = models.IntegerField(validators=[MaxValueValidator(999)])

    # Imperial (auto-generated)
    height_imperial   = models.CharField(max_length=10, editable=False, default="")
    reach_imperial    = models.CharField(max_length=6, editable=False, default="")
    
    division          = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        # Generate imperial values from metric fields
        self.height_imperial = metric_to_imperial(float(self.height_metric))
        self.reach_imperial = format_reach_imperial(float(self.reach_metric))
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.first_name} {self.alias} {self.last_name}"
        )

class FightRecord(models.Model):
    # 1–1 link to Boxer via PK
    boxer  = models.OneToOneField(
        Boxer,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="fight_record"
    )
    wins   = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    draws  = models.PositiveIntegerField(default=0)
    wins_by_knockout = models.PositiveIntegerField(default=0)
    losses_by_knockout = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Record of {self.boxer}: {self.wins}-{self.losses}-{self.draws}"

class BoxerStats(models.Model):
    # 1–1 link to Boxer via PK
    boxer     = models.OneToOneField(
        Boxer,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="stats"
    )
    strength  = models.PositiveSmallIntegerField()
    speed     = models.PositiveSmallIntegerField()
    endurance = models.PositiveSmallIntegerField()
    reflex    = models.PositiveSmallIntegerField()
    heart     = models.PositiveSmallIntegerField()
    boxing_iq = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Stats of {self.boxer}"
