# Florist

## Programmeringsspråk

#### HTML
#### CSS
#### JavaScript med JQuery



## Utvecklingsmiljöstandard

#### Editor 
**Valfri**

#### Browser 
**Firefox/Chromium**

#### OS 
**Linux: Ubuntu 20.04.1 LTS**

För att kunna köra testerna måste ett par paket vara installerade.
`apt update -qq && apt install -yqq jq`



## Kodningsstandard

#### Kod
+ K&R indentering om inget annat har specificerats
+ 4 spaces ska användas vid indentering
+ Om det är delar som är komplicerade, ska de vara extra kommenterade utöver dokumentationen.
+ Koden ska vara städad, t.ex. ingen gammal kod i kommentarer.
+ Övrig “officiell” kodningsstandard ska också följas
#### CSS
+ Onödiga statements ska tas bort, se till att det inte finns något som blir överskrivet och sedan bara ligger kvar.
+ kebab-case
+ Om det går, undvik !important
+ Ska vara bra strukturerat
+ Tydliga klass/id-namn
+ Börja med mobilstorlek och jobba uppåt
#### HTML
+ Validering (Ska utföras av automatiska tester)
+ Självstängande HTML taggar ska ha ett slash i slutet.
+ Indentering i öppnade taggar
#### JavaScript
+ camelCase
+ Nyare standard ska användas, t.ex. let, const
+ jQuery ska oftast användas för att minska kod och göra den effektiv.
+ När typerna är säkra ska triple equals användas
+ Nyare sättet för anonyma funktioner ska användas (Arrow functions)



## Definition of Done 

#### Generellt
+ Allt som görs ska på något sätt kunna presenteras.
#### Dokument
+ Alla har läst igenom, förstår och håller med.
+ Dokumenten ska vara kompletta, ska täcka hela backloggen i skrivandes stund.
#### Kod
+ Tester ska vara skrivna och gröna
+ Kodningsstandard & programmeringsspråk dokumenten ska följas.
+ Alla ska ha läst igenom koden och dokumentation samt förstå dessa.
+ Om de behövs, ska användartester ha genomförts.
+ Klappa kapitalist-robin och be om förlåtelse för koden
#### Versionshantering 
+ Alla CI/CD verktyg som behövs ska vara aktiverade

Static code analysis

Automatic tests

Static Application Security Testing (SAS
