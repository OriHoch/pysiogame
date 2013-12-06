# -*- coding: utf-8 -*-

#this is a list of words used by the word builder and word maze games and possibly
#other games built in the future
#these words are a naive translation of a part of most commonly used words in English
#in each sub-list in the list di first number is a number of words in the sublist
#to aviod counting it every time the list is selected
#the sublists are consisting of words with len() of 3 - 10
#I think the way of going about internationalization here would be to create a new list
#with words most commonly used in your language rather than translating the English version

#I am not sure if they are appriopriate for children, but if anyone is interested we can try to built something more suitable or if you like you can try to edit this list - remove the words that you think are either not in Finnish or are not suitable for under 10 years old children and send it back to the email address shown at the start of the game.

#If you have a better list please send it to me and I will format it and add it to the game. 

#this is a very naive translation from google translate - only resorted and counted

di = [[12, 'hän', 'iho', 'iso', 'isä', 'kun', 'maa', 'nyt', 'ohi', 'sai', 'syö', 'toi', 'työ'],
[32, 'alas', 'alku', 'ansa', 'arvo', 'auto', 'haju', 'hyvä', 'itse', 'juna', 'jätä', 'kala', 'kesä', 'kone', 'kuva', 'kylä', 'käsi', 'levy', 'meni', 'mikä', 'muut', 'näki', 'ohut', 'pala', 'pidä', 'puro', 'runo', 'sama', 'suun', 'tapa', 'tule', 'tuli', 'usko'],
[80, 'aikoo', 'aivot', 'antoi', 'aseet', 'asema', 'ehdot', 'esiin', 'harja', 'hidas', 'huilu', 'huopa', 'ilman', 'jalat', 'jonka', 'juoni', 'kaksi', 'kohta', 'kohti', 'korsi', 'kukka', 'kulta', 'kuule', 'kuuli', 'kuusi', 'kyllä', 'kysyi', 'laaja', 'laiva', 'lakko', 'laulu', 'lause', 'liesi', 'liike', 'lukea', 'luumu', 'malli', 'matka', 'mieli', 'muoto', 'mutta', 'neste', 'nokka', 'nopea', 'paino', 'paras', 'pauke', 'pelko', 'pestä', 'pieni', 'pihvi', 'piste', 'poika', 'puhua', 'pysyä', 'päivä', 'reikä', 'sanat', 'sanoi', 'seimi', 'selaa', 'sinun', 'sähkö', 'sänky', 'tahra', 'tavua', 'tehty', 'testi', 'tiesi', 'tiili', 'tulee', 'tulos', 'tunne', 'tyhjä', 'vakaa', 'verta', 'vielä', 'viiva', 'vuoto', 'vähän', 'väärä'],
[78, 'aineet', 'grilli', 'harmaa', 'hoitaa', 'häipyä', 'jatkaa', 'joskus', 'jotain', 'juoksi', 'jyrkkä', 'kaappi', 'kaavio', 'kaikki', 'kangas', 'kanssa', 'karhea', 'karjaa', 'kasvit', 'kaunis', 'kenttä', 'kerran', 'kiilto', 'kirkas', 'kytkin', 'lattia', 'lausua', 'liekki', 'linnut', 'liukas', 'löysää', 'maissi', 'marssi', 'matala', 'meidän', 'merkki', 'miehet', 'mitään', 'muutos', 'nauhat', 'niellä', 'nukkua', 'numero', 'nähnyt', 'paarit', 'painaa', 'paitsi', 'peikko', 'pilata', 'pusero', 'putken', 'rengas', 'rohkea', 'ruokaa', 'saalis', 'siellä', 'sileää', 'sitten', 'sokeri', 'suunta', 'synkkä', 'sääntö', 'taitoa', 'tiedot', 'tiukka', 'toinen', 'totuus', 'tukkia', 'tänään', 'tärkeä', 'täytyy', 'täällä', 'useita', 'vaikea', 'valmis', 'vedota', 'viitta', 'vuoret', 'ylpeys'],
[50, 'aavikko', 'alentua', 'crumbia', 'ehdotti', 'enemmän', 'energia', 'etelään', 'hyppäsi', 'hyökätä', 'jälkeen', 'kalmari', 'kokeilu', 'kokemus', 'koskaan', 'kuollut', 'kävellä', 'leikata', 'luonnos', 'luvulla', 'metalli', 'milloin', 'muistaa', 'odottaa', 'ohjelma', 'ongelma', 'piikivi', 'pisamia', 'polttaa', 'potkuri', 'prinssi', 'purista', 'päättää', 'raastaa', 'röyhelö', 'sekoita', 'siepata', 'sisällä', 'sivulle', 'sokkona', 'tiputus', 'todiste', 'tohveli', 'vahvuus', 'vakooja', 'vastaus', 'välillä', 'yhdiste', 'yleinen', 'ymmärrä', 'ärjäisy'],
[39, 'hallitus', 'hedelmät', 'hitaasti', 'jokainen', 'kaluston', 'kasvavat', 'katsella', 'kehdosta', 'korostaa', 'koukerot', 'kriketti', 'kuorsata', 'kuuntele', 'lausunto', 'mansikka', 'ongelmia', 'paikalla', 'pelottaa', 'piirtäen', 'punainen', 'reunalla', 'sammakko', 'seuraava', 'skannaus', 'sprintti', 'sulhasen', 'suojella', 'syntynyt', 'tutkijat', 'tyhjästä', 'vaatteet', 'valvonta', 'varrella', 'venyttää', 'verhottu', 'vieressä', 'välipala', 'yhteinen', 'yhtäkkiä'],
[28, 'edustavat', 'erilainen', 'hajoamaan', 'hiljainen', 'huoneessa', 'jäljittää', 'kahdeksan', 'kaltevuus', 'keinuttaa', 'kotkottaa', 'kuukautta', 'laitokset', 'löydetään', 'menetelmä', 'miljoonaa', 'mörökölli', 'näytetään', 'runsaasti', 'sanakirja', 'sivuliike', 'säikähtää', 'tehtaissa', 'tuhansien', 'tuijottaa', 'tunnukset', 'uudelleen', 'venytetty', 'viruminen'],
[14, 'adjektiivi', 'hyväksytty', 'hyönteisiä', 'jännittävä', 'kehittynyt', 'liitutaulu', 'paikallaan', 'professori', 'ristiriita', 'sotilaiden', 'sprinkleri', 'teollisuus', 'tuotteiden', 'varastossa']]
