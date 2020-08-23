---
layout:	post
title:	"Sichtbare Musik"
lang: de
tags: kunst mathe informatik
ref: apollon
date:	2018-07-26 00:10:31 -0500
audience: everyone
excerpt:
---
In meinem erstem richtigen Post will ich ein Projekt teilen, das ich im letztem Semester für mein Flötenstudio gemacht habe. Erst ein bisschen Hintergrund:

### Die Musik
Francis Poulenc (1899-1963)[\[1\]](#references) war ein Französicher Pianist und Komponist, dessen Musik ein wichtiger Teil des Flötenrepertoire ist. Er schrieb viele Sonatinas und andere klavierbegleitete Stücke für die Flöte. Fast alle dieser Werke sind mehrere Seiten lang, doch eins ist besonders: ein Stück für Solo-Flöte mit dem Titel [„Un joueur de flûte berce les ruines"](../../../files/blog/Poulenc.pdf) („Ein Flötenspieler lullt die Ruinen ein”). Das Stück ist ungewöhnlich kurz (nur eine Seite lang bzw. vier Zeilen, bzw. dreizehn Takte) und ist deshalb ein guter Startpunkt, aus dem man weitere Kunststücke kreieren kann.

### Die Mathematik 
Fraktale sind eine der kunstvollsten Teile der Mathematik. Fraktale sind geometrische Objekte die sich selbst sehr ähnlich sind; z.B. können sie aus verkleinerten kopien von sich selbst bestehen. In diesem Fall kann man das Objekt immer weiter vergrößern, und wieder und wieder die selben Muster sehen. Fraktale kommen in der Natur häufig vor: bei Schneeflocken, Ananas-früchten, und Proteinen, unter anderem. Meiner Meinung nach, ist das ein Hinweis, dass Mathematik die Sprache des Universums ist.  
Ein Fraktal, den ihr vielleicht schonmal gesehen habt, ist das Sierpinski-Dreieck:
![Das Sierpinski-Dreieck](../../../files/blog/sierpinski.png)  
Die Makrostruktur dieses Dreiecks besteht aus vier kleieneren Dreiecken. Drei davon sind weiterhin selber kopien des ganzem Sierpinski-Dreiecks, viermal verkleinert. 

Apollonische Kreispackungen sind ein anderes Beispiel für Fraktale. Sie werden von drei Nummern erzeugt, die die Krümmung (den Kehrwert des Radius) von drei Kreisen repräsentieren. Diese drei Kreise bestimmen also die Makrostruktur des Fraktals. Wie bei dem Sierpinski-Dreieck wird der rest durch Rekursion gemalt. Hier sehen sie Kreispackungen die von verschiedenen Gruppen von vier Nummern erzeugt werden.  
![Krümmungen (-1, 2, 2, 3)](../../../files/blog/apollon1_2_2_3.png "Kreispackung mit Krümmungen (-1, 2, 2, 3) erzeugt") ![Krümmungen (-3, 5, 8, 8)](../../../files/blog/apollon3_5_8_8.png "Kreispackung mit Krümmungen (-3, 5, 8, 8) erzeugt") ![Krümmungen (-12, 25, 25, 28)](../../../files/blog/apollon12_25_25_28.png "Kreispackung mit Krümmungen (-12, 25, 25, 28) erzeugt") ![Krümmungen (-6, 10, 15, 19)](../../../files/blog/apollon6_10_15_19.png "Kreispackung mit Krümmungen (-6, 10, 15, 19) erzeugt") ![Krümmungen (-10, 18, 23, 27)](../../../files/blog/apollon10_18_23_27.png "Kreispackung mit Krümmungen (-10, 18, 23, 27) erzeugt")
##### _Bilder von Todd Stedl (NefariousPhD) \[GFDL ([http://www.gnu.org/copyleft/fdl.html](http://www.gnu.org/copyleft/fdl.html)) oder CC BY-SA 4.0 ([https://creativecommons.org/licenses/by-sa/4.0](https://creativecommons.org/licenses/by-sa/4.0))\], von Wikimedia Commons_

Augenblick! Vier Nummern?! Habe ich nicht gerade gesagt, dass diese Kreispackungen von drei Nummern erzeugt werden?  
 
In diesen Kreispackungen ist eine vierte Nummer angegeben, aber sie ist überflüssig. Wir brauchen eigentlich nur die ersten drei Nummern von jeder Gruppe um einen dieser Fraktale zu erzeugen; die vierte Nummer ist die Krümmung eines Kreises tangential zu allen drei vorherigen Kreisen. Die können wir auch selber mit dem Satz von Descartes finden:

**Satz.** Gegeben sind vier einender berührenden Kreise \\(C_1\\), \\(C_2\\), \\(C_3\\), and \\(C_4\\). Ihre Krümmungen erfüllen die Gleichung
\\[2({k_1}^2+{k_2}^2+{k_3}^2+{k_4}^2) = (k_1+k_2+k_3+k_4)^2\\]

Diese Gleichung kann man so umschreiben:
\\[k_4 = k_1 + k_2 + k_3 \pm 2\sqrt{k_1k_2+k_2k_3+k_1k_3}\\]
(Eine detailierte Erklärung finden sie [in diesem Englischen Blogeintrag](https://euler.genepeer.com/from-herons-formula-to-descartes-circle-theorem).)  

Also, wenn wir nur die Nummern (-1, 2, 2) wissen, können wir auch die vierte Nummer bestimmen:
\\[k_4 = -1 + 2 + 2 \\pm 2(0)\\]
\\[k_4 = 3\\]

Das wichtige hier ist dass das ganze Fraktal durch drei Nummern definiert werden kann. (Details, inkl. genau wie sie ihre einene Kreispackung malen können finden sie in [diesem Englischen wikiHow Artikel](https://www.wikihow.com/Create-an-Apollonian-Gasket).)

### Die Informatik
Im Internet gibt es viele Programme und Webseiten die ihnen helfen können, euren egeinen Fraktal herzustellen. Eine solche Seite ist Ludger Sandigs [Apollonische Kreispackung Erzeuger](http://lsandig.org/cgi-bin/apollon/index.cgi) und sein [dazugehöriger Blogeintrag](https://lsandig.org/blog/2014/08/apollon-python/). Die Seite ist eine Online-version von seinem Kommandozeilenprogramm [apollon auf GitHub](https://github.com/lsandig/apollon), welchem ich für dieses Projekt benutzt habe.

### Der Coole Teil
Wie gehört das alles zusammen?

Die Idee hinter all diesem war, Poulencs kurzes Flötenstück als anfang für ein neues Kunststück zu benutzen. Wegen meinem Interesse an Mathematik wollte ich die Musik in ein Fraktal umwandeln, zum Teil auch weil ich ahnte, dass fast niemand außer Mathematikern denkt, dass Mathe schön sein kann.
Es gibt viele Arten von Fraktalen, von denen ich wählen konnte. Am Ende habe ich Apollonische Kreispackungen ausgewählt, weil ich dachte solche Kreise konnten den sanften, verbundenen Stil von Poulencs Wiegenlied am besten räpresentiert.   
Als nächstes teilte ich das Stück in sechs musikalische Phrasen. Jede von diesen Phrasen wurde von einer verschiedenen Kreispackung räpresentiert, die in der folgenden Weise erzeugt wurde. Jede Note in der Phrase bekam in korrespondenz zu ihrer Länge eine Nummer: 2 für eine Halbe, 4 für eine Viertel, 8 für eine Achtel, usw. In dieser Maniere würden lebhaftere Phrasen (mit mehr kleinen Noten) Kreise mit höheren Krümmungen, und deshalb geringere Radien, erzeugen. Diese Nummern wurden dann in Dreiergruppen gestellt. Z.B. war die erste Gruppe der ersten Phrase (4, 8, 8), bzw. eine Viertel und zwei Achtel danach. Ich hatte Glück, denn zum großteil teilten sich die Phrasen gut (die letzten zwei waren ein bisschen problematisch; im ersten Fall, habe ich so getan, als ob eine Achtelpause eine Note wäre, und im zweiten Fall beachtete ich eine ganze Note mit Aufhaltezeichen als zwei ganze Noten).  
Jetzt hatte ich für jede Phrase mehrere Fraktale (im Fall der ersten Phrase waren es drei Fraktale die von (4, 8, 8), (4, 4, 4), und (8, 8, 2) erzeugt wurden). Ich habe entschieden, diese in der selben Reihenfolge ineinander zu fügen, bzw. den (4, 4, 4) Fraktal in den größten Kreis des (4, 8, 8) Fraktals, und den (8, 8, 2) Fraktal in den größten Kreis des (4, 4, 4) Fraktals (das in dem (4, 8, 8) eingefügt geworden war). Dieses zusammengesetzte Fraktal wurde das Fraktal für die Phrase.  
Jeder dieser sechs Phrasenfraktale wurden am Ende in einem großen Fraktal gesetzt, der das ganze Stück räpresentieren würde. Dieses größte Fraktal wurde einfach mit den Nummern generiert, die meiner Meinung nach am besten aussahen (leider nichts Mathematisches dabei, sorry!). Er sieht aus wie ein großer Kreis der von mehreren kleineren geringelt ist, und in diese kleinere Kreise habe ich die sechs Phrasenfraktale von links nach rechts gesetzt. Das Endprodukt sehen sie hier:   

![Poulenc Fraktal](../../../files/blog/poulenc-gasket.jpg)  

Vielleicht haben sie gemerkt, das dieses Fraktal nur mit dem Rythmus des Stücks generiert worde - Musik ist aber viel mehr als nur Rhythmus! In der Zukunft werde ich hoffentlich dieses Projekt wieder besuchen und andere Eigenschaften (z.B. Notennamen, Oktaven, Dynamikanweisungen, und Artikulationsarten) des Stückes in einem neuen, besseren Fraktal einarbeiten.

#### Literatur
1. Francis Poulenc. (2018). Von [https://www.poulenc.fr/en/?Biography](https://www.poulenc.fr/en/?Biography).
