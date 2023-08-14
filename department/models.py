from django.db import models

# from accounts.models import User

# from folder.models import Folder

# Create your models here.


# class Department(models.Model):
#     name = models.CharField(max_length=255, blank=False)
#     description: models.CharField(max_length=255, blank=True, null=True)
#     # staff = models.ManyToManyField(User, related_name="staff")
#     # folder = models.ManyToManyField(Folder, related_name="departments")
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name


# <!-- book_detail.html -->
# <form>
#     <label for="authors">Authors:</label>
#     <select name="authors" id="authors" multiple>
#         {% for author in book.authors.all %}
#             <option value="{{ author.id }}">{{ author.name }}</option>
#         {% endfor %}
#     </select>
# </form>
