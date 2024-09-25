from django.db import models

class Department(models.Model):
    d_name = models.CharField(max_length=100)
    d_location = models.CharField(max_length=100)
    
    def __str__(self): 
        return "%s - %s"%(self.d_name, self.d_location)
    
    
class Role(models.Model):
    r_name = models.CharField(max_length=100)
    
    def __str__(self): 
        return "%s"%(self.r_name)
    
class Employee(models.Model):
    sno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    salary = models.IntegerField(default=10000)
    bonus = models.IntegerField(default=10000)
    phone_number = models.IntegerField(default=10000)
    hire_date = models.DateField()
    
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    
    def __str__(self): 
        return "%s %s"%(self.first_name, self.last_name)