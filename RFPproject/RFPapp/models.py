from django.db import models

class Kapela(models.Model):
    id = models.IntegerField(primary_key=True)
    jmeno = models.CharField(max_length=45, unique=True)
    zanr = models.CharField(max_length=45)

    def __str__(self):
        return self.jmeno

class Osoba(models.Model):
    id = models.AutoField(primary_key=True)
    jmeno = models.CharField(max_length=45)
    prijmeni = models.CharField(max_length=45)
    kapela_jmeno = models.ForeignKey(Kapela, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"

class Pisnicka(models.Model):
    id = models.AutoField(primary_key=True)
    jmeno_pisne = models.CharField(max_length=45)
    zanr = models.CharField(max_length=45)
    kapela_jmeno = models.ForeignKey(Kapela, on_delete=models.CASCADE)

    def __str__(self):
        return self.jmeno_pisne