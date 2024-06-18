from django.db import models

class Kapela(models.Model):
    jmeno = models.CharField(max_length=45, unique=True, verbose_name='Jméno kapely')
    zanr = models.CharField(max_length=45, verbose_name='Žánr kapely')
    obrazek = models.ImageField(upload_to='img/kapely', blank=True, null=True, verbose_name='Fotka kapely')
    popis = models.TextField(blank=True, verbose_name='Popis kapely')

    class Meta:
        ordering = ['jmeno']
        verbose_name = 'Kapela'
        verbose_name_plural = 'Kapely'

    def __str__(self):
        return f"{self.jmeno} - {self.zanr}"

class Osoba(models.Model):
    jmeno = models.CharField(max_length=45, verbose_name='Jméno osoby')
    prijmeni = models.CharField(max_length=45, verbose_name='Příjmení osoby')
    kapela_jmeno = models.ForeignKey(Kapela, on_delete=models.CASCADE)

    class Meta:
        ordering = ['prijmeni', 'jmeno']
        verbose_name = 'Osoba'
        verbose_name_plural = 'Osoby'

    def seznam_osob(self):
        return Osoba.objects.filter(kapela_jmeno=self)

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"

class Pisnicka(models.Model):
    jmeno_pisne = models.CharField(max_length=45, verbose_name='Jméno písně')
    zanr = models.CharField(max_length=45, verbose_name='Žánr písně')
    kapela_jmeno = models.ForeignKey(Kapela, on_delete=models.CASCADE)

    class Meta:
        ordering = ['jmeno_pisne']
        verbose_name = 'Píseň'
        verbose_name_plural = 'Písně'

    def seznam_pisnicek(self):
        return Pisnicka.objects.filter(kapela_jmeno=self)