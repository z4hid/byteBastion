# A model that stores the result of a malware scan
from django.db import models

class MalwareDetection(models.Model):
    """
    Stores the result of a malware scan.

    Attributes:
        image_name (str): The name of the image that was scanned.
        timestamp (datetime.datetime): The time the scan was done.
        response_status (int): The status of the scan.
        response_data (str): The response data from the scan.
        error_message (str): An error message if something went wrong.
    """

    image_name = models.CharField(
        max_length=255,
        help_text="The name of the image that was scanned",
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        help_text="The time the scan was done",
    )
    response_status = models.IntegerField(
        help_text="The status of the scan",
    )
    response_data = models.TextField(
        help_text="The response data from the scan",
    )
    error_message = models.TextField(
        blank=True,
        null=True,
        help_text="An error message if something went wrong",
    )

    def __str__(self):
        """
        Returns a string representation of the model.

        Returns:
            str: A string representation of the model.
        """
        return f"{self.image_name} - {self.timestamp}"

