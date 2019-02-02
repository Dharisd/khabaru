from scrapers import scrapers

s = scrapers()
mihaaru = s.mihaaru(40722) 
sun = s.sun(114916) 
avas = s.avas(53047) 
vfp = s.vfp(81482)
psm = s.psm(37250)

print(mihaaru["headline"])        
print(avas["headline"])  
print(vfp["headline"])        
print(psm["headline"])
print(sun)    
