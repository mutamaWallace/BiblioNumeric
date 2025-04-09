from django.db import models
from campus.models import Campus

# Create your models here.
class Universite(models.Model):
    PAYS_CHOICES = [
    ('DZ', 'Algérie'),
    ('AO', 'Angola'),
    ('BJ', 'Bénin'),
    ('BW', 'Botswana'),
    ('BF', 'Burkina Faso'),
    ('BI', 'Burundi'),
    ('CM', 'Cameroun'),
    ('CV', 'Cap-Vert'),
    ('CF', 'République Centrafricaine'),
    ('TD', 'Tchad'),
    ('KM', 'Comores'),
    ('CG', 'Congo-Brazzaville'),
    ('CD', 'Congo-Kinshasa'),
    ('DJ', 'Djibouti'),
    ('EG', 'Égypte'),
    ('GQ', 'Guinée équatoriale'),
    ('ER', 'Érythrée'),
    ('SZ', 'Eswatini'),
    ('ET', 'Éthiopie'),
    ('GA', 'Gabon'),
    ('GM', 'Gambie'),
    ('GH', 'Ghana'),
    ('GN', 'Guinée'),
    ('GW', 'Guinée-Bissau'),
    ('KE', 'Kenya'),
    ('LS', 'Lesotho'),
    ('LR', 'Liberia'),
    ('LY', 'Libye'),
    ('MG', 'Madagascar'),
    ('MW', 'Malawi'),
    ('ML', 'Mali'),
    ('MR', 'Mauritanie'),
    ('MU', 'Maurice'),
    ('MA', 'Maroc'),
    ('MZ', 'Mozambique'),
    ('NA', 'Namibie'),
    ('NE', 'Niger'),
    ('NG', 'Nigéria'),
    ('RW', 'Rwanda'),
    ('ST', 'Sao Tomé-et-Principe'),
    ('SN', 'Sénégal'),
    ('SC', 'Seychelles'),
    ('SL', 'Sierra Leone'),
    ('SO', 'Somalie'),
    ('ZA', 'Afrique du Sud'),
    ('SS', 'Soudan du Sud'),
    ('SD', 'Soudan'),
    ('TZ', 'Tanzanie'),
    ('TG', 'Togo'),
    ('TN', 'Tunisie'),
    ('UG', 'Ouganda'),
    ('ZM', 'Zambie'),
    ('ZW', 'Zimbabwe'),
]
    
    VILLES_CHOICES = [
    ('ALGIERS', 'Alger'),
    ('CARTAGE', 'Carthage'),
    ('LAGOS', 'Lagos'),
    ('NAIROBI', 'Nairobi'),
    ('CAIRO', 'Le Caire'),
    ('DAKAR', 'Dakar'),
    ('ADDIS_ABABA', 'Addis-Abeba'),
    ('KAMPALA', 'Kampala'),
    ('TUNIS', 'Tunis'),
    ('HARARE', 'Harare'),
    ('ACCRA', 'Accra'),
    ('KIGALI', 'Kigali'),
    ('BAMAKO', 'Bamako'),
    ('LUANDA', 'Luanda'),
    ('BANGUI', 'Bangui'),
    ('BUJA', 'BUJUMBURA'),
    ('ANTANANARIVO', 'Antananarivo'),
    ('PORTO_NOVO', 'Porto-Novo'),
    ('BRAZZAVILLE', 'Brazzaville'),
    ('KINSHASA', 'Kinshasa'),
    ('FREETOWN', 'Freetown'),
    ('MONROVIA', 'Monrovia'),
    ('MASERU', 'Maseru'),
    ('MBABANE', 'Mbabane'),
    ('GABORONE', 'Gaborone'),
    ('MAPUTO', 'Maputo'),
    ('NOUAKCHOTT', 'Nouakchott'),
    ('NIAMEY', 'Niamey'),
    ('DJIBOUTI', 'Djibouti'),
    ('BISSAU', 'Bissau'),
    ('TANANARIVE', 'Tananarive'),
    ('LILONGWE', 'Lilongwe'),
    ('KAMPALA', 'Kampala'),
    ('HARARE', 'Harare'),
    ('BLOEMFONTEIN', 'Bloemfontein'),
    ('PRETORIA', 'Pretoria'),
    ('CAPE_TOWN', 'Le Cap'),
]
    universite= models.CharField(max_length=50)
    pays = models.CharField(max_length=59, choices=PAYS_CHOICES)
    ville = models.CharField(max_length=50, choices=VILLES_CHOICES)
    email = models.EmailField(max_length=20)
    site_web = models.URLField(max_length=30)
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)
    
    def __str__(self):
       return self.universite
   
class Faculte(models.Model):
    faculte= models.CharField(max_length=50)
    universite = models.ForeignKey(Universite, on_delete=models.PROTECT)
    def __str__(self):
       return self.faculte
   
   
class Departement(models.Model):
    departement= models.CharField(max_length=50)
    faculte = models.ForeignKey(Faculte, on_delete=models.PROTECT)
    def __str__(self):
        return self.departement
class Class(models.Model):
    faculte = models.ForeignKey(Faculte, on_delete=models.PROTECT, null=True)
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT, null=True)
    niveau= models.CharField(max_length=50)
     
