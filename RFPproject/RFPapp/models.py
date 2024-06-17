from django.db import models

class Kapela(models.Model):
    jmeno = models.CharField(max_length=45, unique=True)
    zanr = models.CharField(max_length=45)
    obrazek = models.ImageField(upload_to='img/kapely', blank=True, null=True)
    popis = models.TextField(blank=True)

    def __str__(self):
        return f"{self.jmeno} - {self.zanr}"

class Osoba(models.Model):
    jmeno = models.CharField(max_length=45)
    prijmeni = models.CharField(max_length=45)
    kapela_jmeno = models.ForeignKey(Kapela, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"

class Pisnicka(models.Model):
    jmeno_pisne = models.CharField(max_length=45)
    zanr = models.CharField(max_length=45)
    kapela_jmeno = models.ForeignKey(Kapela, on_delete=models.CASCADE)

    def seznam_osob(self):
        return Osoba.objects.filter(kapela_jmeno=self)

    def seznam_pisnicek(self):
        return Pisnicka.objects.filter(kapela_jmeno=self)