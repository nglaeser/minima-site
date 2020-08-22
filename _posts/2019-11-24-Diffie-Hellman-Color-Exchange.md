---
layout:	post
title:	"Diffie-Hellman Color Exchange"
lang: en
tags: cs math
ref: dh
date:	2019-11-24 18:16:33 -0500
audience: everyone
excerpt:
---

I'd like to take a foray into public key cryptography by introducing a metaphor for the Diffie-Hellman Key Exchange. Introduced by Diffie and Hellman in their 1976 paper ["New Directions in Cryptography"](https://ee.stanford.edu/%7Ehellman/publications/24.pdf) and based on the concept of [Merkle's puzzles](http://www.merkle.com/1974/PuzzlesAsPublished.pdf), the DH Key Exchange is one of the first public-key protocols. It is used to exchange private information (namely, a key) over a public/insecure channel.

If you don't realize how amazing and counter-intuitive this concept is, read that sentence again. I'm saying that you and I could stand in a room full of a bunch of other people, even people who might not like us very much and would be happy to sabotage us, and, just by shouting across the room so everyone can hear, arrive at a piece of information no one else can figure out.

Okay, so how can that be? Here's where the metaphor comes in. Leaving aside modular arithmetic and group theory at first, I'll describe this system using colors instead. Then, if you're interested in knowing the details of the real system, you can read on to the last section.

## Diffie-Hellman Color Exchange

In the interest of making this metaphor seem somewhat applicable, I'll describe a bit of a far-fetched scenario. Suppose Alice and Bob are sitting in a coffee shop. Alice is about to have a baby, and she and Bob are discussing what color to paint the baby's new room. They want to make sure it'll enhance the lighting, match the cradle they already bought, and complement the rest of the house's décor. The problem is, Alice has spotted her enemy Eve sitting at a nearby table, and Alice is worried that if Eve knows the color of the room, she'll show up at the baby shower with a really ugly vase or some similar gift in the exact color that will clash with the room.

So Alice and Bob need to figure out a way to arrive at a common color without Eve knowing what that color is, all while saying everything out loud in way that anyone in the coffee shop (including Eve) can hear. Enter the Diffie Hellman *Color* Exchange (DHCE)[\*](#footnote).  

First, Alice and Bob pick a common *base color*, for example <a style="color: #FF0000">**red**</a>. Now Alice and Bob each choose a *secret color*. For Example, Alice could pick <a style="color: #FF9900">**orange**</a> and Bob <a style="color: #FF99FF">**light pink**</a>. Now Alice and Bob each blend the base color with their secret color (if the colors are simple enough, maybe they can do it mentally, or since our scenario is already ridiculous enough we could say they bring literal paints and brushes and palettes, or they can use a color blender like [this one](https://meyerweb.com/eric/tools/color-blend/) on their phones). Once they've arrived at these *intermediate colors*, they share them with each other and switch. In our example, Alice gives Bob <a style="color: #FF4D00">**this red-orange**</a> while Bob passes this <a style="color: #FF4D80">**hot pink**</a> to Alice. Now for the final step: Alice and Bob once again blend their secret colors into these new intermediate colors, and &mdash; guess what &mdash; they have arrived at a final, shared, and secret color: the <a style="color: #FF7340">**color of the baby's new room**</a>!

View: 
<input type="radio" id="globalView" name="view" value="global" checked><label for="global">Global</label>
<input type="radio" id="aliceView" name="view" value="alice"><label for="alice">Alice</label>
<input type="radio" id="bobView" name="view" value="bob"><label for="bob">Bob</label>
<input type="radio" id="eveView" name="view" value="eve"><label for="eve">Eve</label>

<input type="color" id="baseColor" value="#ff0000">
<label for="baseColor">Base Color</label>

<p>Secret colors:</p>
<input class="knownByAlice" type="color" id="aliceSecret" value="#ff9900">
<label for="aliceSecret">Alice</label><br/>
<input class="knownByBob" type="color" id="bobSecret" value="#ff99ff">
<label for="bobSecret">Bob</label><br/>

<p>Intermediate colors:</p>
<div style="width:50px;height:1em;background-color:#ff4d00;margin-left:6px;margin-right:6px;float:left;" id="aliceIntermed"></div><label for="aliceIntermed" style="float:left;">Alice</label><br/>
<!--input class="public" type="color" id="aliceIntermed" value="#ff4d00">
<label for="aliceIntermed">Alice</label><br/-->
<div style="width:50px;height:1em;background:#ff4d80;margin-left:6px;margin-right:6px;float:left;" id="bobIntermed"></div><label for="aliceIntermed" style="float:left;">Bob</label><br/>
<!--input class="public" type="color" id="bobIntermed" value="#ff4d80">
<label for="bobIntermed">Bob</label><br/-->

<p>Final:</p>
<input class="aliceFinal" type="color" id="aliceFinal" value="#ff7b40"> = Bob's intermediate + Alice's secret<br/>
<input class="bobFinal" type="color" id="bobFinal" value="#ff7b40"> = Alice's intermediate + Bob's secret<br/>

<script>
var baseColor;
var defaultBase = "#ff0000";
var aliceSecret;
var defaultAS = "#ff9900";
var bobSecret;
var defaultBS = "#ff99ff";
var aliceIntermed;
var bobIntermed;
var aliceFinal;
var bobFinal;
window.addEventListener('load', init, false);

function init(){
    baseColor = document.querySelector("#baseColor");
    baseColor.value = defaultBase;
    aliceSecret = document.querySelector("#aliceSecret");
    aliceSecret.value = defaultAS;
    bobSecret = document.querySelector("#bobSecret");
    bobSecret.value = defaultBS;
    aliceIntermed = document.querySelector("#aliceIntermed");
    bobIntermed = document.querySelector("#bobIntermed");
    aliceFinal = document.querySelector("#aliceFinal");
    bobFinal = document.querySelector("#bobFinal");

    aliceIntermed.value = colorMix(baseColor.value, 1, aliceSecret.value, 1);
    bobIntermed.value = colorMix(baseColor.value, 1, bobSecret.value, 1);
    aliceFinal.value = colorMix(bobIntermed.value, 2, aliceSecret.value, 1);
    bobFinal.value = colorMix(aliceIntermed.value, 2, bobSecret.value, 1);

    baseColor.addEventListener("change", changeBaseColor, false);
    aliceSecret.addEventListener("change", changeAS, false);
    bobSecret.addEventListener("change", changeBS, false);
}

function changeBaseColor(event) {
    baseColor = document.querySelector("#baseColor");
    baseColor.value = event.target.value;
    aliceSecret = document.querySelector("#aliceSecret");
    bobSecret = document.querySelector("#bobSecret");

    aliceIntermed = document.querySelector("#aliceIntermed");
    bobIntermed = document.querySelector("#bobIntermed");
    aliceFinal = document.querySelector("#aliceFinal");
    bobFinal = document.querySelector("#bobFinal");

    aliceIntermed.value = colorMix(baseColor.value, 1, aliceSecret.value, 1);
    bobIntermed.value = colorMix(baseColor.value, 1, bobSecret.value, 1);
    aliceFinal.value = colorMix(bobIntermed.value, 2, aliceSecret.value, 1);
    bobFinal.value = colorMix(aliceIntermed.value, 2, bobSecret.value, 1);

    alert ("change base color");
}

function changeAS(event) {
  baseColor = document.querySelector("#baseColor");

  aliceIntermed = document.querySelector("#aliceIntermed");
  bobIntermed = document.querySelector("#bobIntermed");
  aliceFinal = document.querySelector("#aliceFinal");
  bobFinal = document.querySelector("#bobFinal");
  var rgb = aliceIntermed.style.backgroundColor;
  rgb = rgb.substr(rgb.indexOf('(')+1, rgb.indexOf(')') - rgb.indexOf('(')-1)
  aliceIntermedColor = "#" + rgb.split(',').map((color) => String("0" + parseInt(color).toString(16)).slice(-2)).join('');
    // alert("foo " + aliceIntermedColor);
  aliceIntermed.style.background = colorMix(baseColor.value, 1, aliceSecret.value, 1);

  var rgb = bobIntermed.style.backgroundColor;
  rgb = rgb.substr(rgb.indexOf('(')+1, rgb.indexOf(')') - rgb.indexOf('(')-1)
  bobIntermedColor = "#" + rgb.split(',').map((color) => String("0" + parseInt(color).toString(16)).slice(-2)).join('');

  aliceFinal.value = colorMix(bobIntermedColor, 2, aliceSecret.value, 1);
  bobFinal.value = colorMix(aliceIntermedColor, 2, bobSecret.value, 1);

}

function changeBS(event) {
  baseColor = document.querySelector("#baseColor");

  // bobIntermed = document.querySelector("#bobIntermed");
  bobIntermed = document.querySelector("#bobIntermed");
  aliceFinal = document.querySelector("#aliceFinal");
  bobFinal = document.querySelector("#bobFinal");
  bobIntermed.style.background = colorMix(baseColor.value, 1, bobSecret.value, 1);
  aliceFinal.value = colorMix(bobIntermed.style.background, 2, aliceSecret.value, 1);
  bobFinal.value = colorMix(aliceIntermed.style.background, 2, bobSecret.value, 1);
}

function updateFirst(event) {
    var p = document.querySelector("p");

    if(p) {
        p.style.color = event.target.value;
    }
}

function colorMix(color1, ratio1, color2, ratio2) {
    // alert("color 1: " + color1 + "color 2: " + color2);
    var R1 = parseInt(color1.substring(1,3),16);
    var G1 = parseInt(color1.substring(3,5),16);
    var B1 = parseInt(color1.substring(5,7),16);

    var R2 = parseInt(color2.substring(1,3),16);
    var G2 = parseInt(color2.substring(3,5),16);
    var B2 = parseInt(color2.substring(5,7),16);

    var r1 = parseInt(ratio1,10);
    var r2 = parseInt(ratio2,10);

    var R = Math.round((R1*r1 + R2*r2)/(r1+r2));
    var G = Math.round((G1*r1 + G2*r2)/(r1+r2));
    var B = Math.round((B1*r1 + B2*r2)/(r1+r2));

    /*var R = Math.round((R1+R2)/2);
    var G = Math.round((G1+G2)/2);
    var B = Math.round((B1+B2)/2);*/

    var Rstring = R.toString(16).padStart(2, '0');
    var Gstring = G.toString(16).padStart(2, '0');
    var Bstring = B.toString(16).padStart(2, '0');

    return "#"+Rstring+Gstring+Bstring;
}
</script>

So, what does this look like from Eve's point of view? Let's assume that Eve hiding behind a newspaper at the next table over and only overhears Alice and Bob's conversation. She can't get a peek of Alice or Bob's secret colors while they're mixing. Here's what she hears:

> Alice & Bob: Let's use red as our base color!  
> Alice: Okay, my intermediate color is red-orange.  
> Bob: Cool, mine is hot pink.  
> [ furious mixing ]  
> Alice: Aww, this is a wonderful color for the baby's room!  
> Bob: I agree! Let's go buy the paint.  

Or maybe something like this, if Alice and Bob like to be very exact:

> Alice & Bob: Let's use #FF0000 as our base color!  
> Alice: Okay, my intermediate color is #FF4D00.  
> Bob: Cool, mine is #FF4D80.  
> [ furious mixing ]  
> Alice: Aww, this is a wonderful color for the baby's room!  
> Bob: I agree! Let's go buy the paint.  

Because Eve isn't able to see Alice and Bob in the act of mixing their secret colors into they shared ones, she has no idea what's going on. Even if she knows the DHCE protocol, she isn't able to figure out Alice or Bob's secret color, so she can't arrive at the final color despite overhearing the intermediate shades.

Obviously, there are a couple of problems with this approach. First of all, the security of DHCE relies on the assumption that Eve can't "unmix" colors. This isn't quite true; pretty much anyone can figure out, after hearing that the base color is red and Alice's intermediate is red-orange, that her secret color is orange.[\*\*](#footnote2) Even if we're using the hex representations, all Eve has to do is understand the formula for averages: if the base color plus the secret A average to #FF4D00, it's not hard to figure out what \\(a\\) is in this equivalence: \\(\frac{FF0000 + a}{2} \equiv FF4D00 \mod 16\\).

Another problem for the real Diffie-Hellman Key Exchange is that it doesn't implement authenticity: nothing stops Eve from putting on an Alice disguise and sitting down at the table with Bob while Alice is in the bathroom, for example.

## Diffie-Hellman Key Exchange

In the real protocol, the Diffie-Hellman *Key* Exchange, Alice and Bob are trying to agree on a key (instead of a color). Once they have this shared piece of secret information, they can use it to encrypt their future messages. Here's how it works.

DH takes place in a multiplicative group modulo \\(p\\): This is a set {0, 1, ..., \\(p\\)}, where \\(p\\) is a prime, along with the operation of multiplication, i.e., you are allowed to multiply any elements of that set with each other. The stipulation, though, is that the answer must land in that set. An example a group modulo some \\(n\\) is the 24-hour system of time. In that case, \\(n = 24\\). Notice that we call midnight 0, and we go all the way up to 23, but as soon as we add another hour, we roll back over to 0. In this group, for example, we can figure out that 5 hours after 8 P.M., i.e., 20:00, is 20 + 5 which is 25. That's not a time though, so we reduce it back into the range 0-23 and we get 25-24 is 1. So 5 hours after 20:00 is 01:00, or 1 A.M. Now if we extend this to any \\(n\\) and multiplication instead of addition, we can work with groups like the multiplicative group modulo the prime \\(5\\), and in that group, \\(2 * 3 \equiv 1 \mod 5\\) and \\(4 * 3 \equiv 2 \mod 5\\). We write this group as \\((\mathbb{Z}/5\mathbb{Z})^\times\\) or more generally as \\((\mathbb{Z}/p\mathbb{Z})^\times\\) for \\(p\\) prime. The \\(\times\\) means we exclude the 0 element. We leave it out because it's special, in a sense: multiplication of any element by 0 automatically returns 0, and then we get kind of stuck in the "black hole" of 0. There's also no way to multiply non-zero elements and get 0.

Another concept you need to know about to understand the algorithm is the idea of a generator of this kind of group. The best way to explain this is by example. Take the group \\((\mathbb{Z}/5\mathbb{Z})^\times\\) that we were using earlier. It contains the elements {1, 2, 3, 4}. Let's go through them one by one and decide whether or not they are a generator of the group.

**1:** \\(1^1 = 1, 1^2 = 1, 1^3 = 1, ...\\)  
**2:** \\(2^1 = 2, 2^2 = 4, 2^3 = 8 \equiv 3 \mod 5, 2^4 = 16 \equiv 1 \mod 5 \\)  
**3:** \\(3^1 = 3, 3^2 = 9 \equiv 4 \mod 5, 3^3 = 27 \equiv 2 \mod 5, 3^4 = 81 \equiv 1 \mod 5 \\)  
**4:** \\(4^1 = 4, 4^2 = 16 \equiv 1 \mod 5, 4^3 = 64 \equiv 4 \mod 5, 4^4 = 256 \equiv 1 \mod 5 \\)

This shows that 2 and 3 are generators, but 1 and 4 are not. Can you guess why?

The answer is that by exponentiating 2 and 3 to various powers \\(k\\), we are able to obtain all of the elements of the group, albeit in the wrong order. 1 and 4, on the other hand, don't have this property: every power of 1 is just 1, and powers of 4 alternate between 4 (which we can also call -1) and 1.

Okay, now that you have the background, here's the protocol. First, Alice and Bob publicly agree on a prime modulus \\(p\\) and generator \\(g\\) of the group \\((\mathbb{Z}/p\mathbb{Z})^\times\\). Next Alice and Bob choose their "secret colors" and use them to calculate and share the "intermediate colors", only now, the colors are actually numbers. Symbolically, we can call Alice's secret \\(a\\) and Bob's secret \\(b\\); then their intermediate colors are calculated as \\(A = g^a \mod p\\) and \\(B = g^b \mod p\\), respectively. Now they exchange \\(A\\) and \\(B\\) and once again "mix in" their secrets, Alice by calculating \\(B^a \mod p\\) and Bob by calculating \\(A^b \mod p\\). The magic is this: \\(B^a \mod p = A^b \mod p\\), since 

\\(B^a \mod p = (g^b)^a \mod p = g^{ba} \mod p = g^{ab} \mod p = (g^a)^b \mod p = A^b \mod p\\).

Let's do an example in the same group we've been using the whole time, the group modulo 5.[\*\*\*](#footnote3) So, \\(p = 5\\) and we can pick either generator; let's go with \\(g = 2\\). Now say Alice picks \\(a = 2\\) and Bob lets \\(b = 3\\). (1 would be a bad choice for either of them, since exponentiation by 1 does nothing.) They calculate the intermediate values, \\(A = 2^2 = 4\\) and \\(B = 2^3 \equiv 3\\), and share them with each other. Now they can both calculate the shared secret:  

 \\(B^a = 3^2 = 9 \equiv 4 \mod 5\\) and \\(A^b = 4^3 = 64 \equiv 4 \mod 5\\)!

##### \*100% made up acronym<a name="footnote"></a>
##### \*\*or maybe you've got acess to an [unmixing machine](https://www.youtube.com/watch?v=j2_dJY_mIys)<a name="footnote2"></a>
##### \*\*\*I'm going to pick very small numbers so we can do this by hand; in reality, users of the DH key exchange would pick very large values.<a name="footnote3"></a>
