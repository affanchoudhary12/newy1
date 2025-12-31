<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Assalamualaikum</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">

<style>
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{
font-family:'Poppins',sans-serif;
background:linear-gradient(180deg,#050505,#0b1d26);
color:#f5f5f5;
}

/* sections = pages */
section{
min-height:100vh;
display:flex;
align-items:center;
justify-content:center;
text-align:center;
padding:50px;
}

/* card */
.card{
background:rgba(255,255,255,0.06);
backdrop-filter:blur(12px);
border-radius:30px;
padding:60px;
max-width:900px;
animation:fadeUp 1.5s ease;
}

@keyframes fadeUp{
from{opacity:0;transform:translateY(50px)}
to{opacity:1;transform:translateY(0)}
}

h1{font-size:52px;letter-spacing:2px}
h2{font-size:34px;margin-bottom:20px}
p{font-size:18px;line-height:1.9;opacity:0.95}

.btn{
margin-top:35px;
padding:14px 38px;
border-radius:40px;
border:1px solid #f5f5f5;
background:transparent;
color:#f5f5f5;
font-size:16px;
cursor:pointer;
transition:0.4s;
}
.btn:hover{
background:#f5f5f5;
color:#000;
}
</style>
</head>

<body>

<!-- PAGE 1 -->
<section id="p1">
<div class="card">
<h1>Mohd Affan</h1>
<br>
<h2>Assalamualaikum 🤍</h2>
<p>
Ye message sirf ek reminder hai,<br>
deen ke hawale se, pyar aur izzat ke saath.
</p>
<button class="btn" onclick="go('p2')">Continue ↓</button>
</div>
</section>

<!-- PAGE 2 -->
<section id="p2">
<div class="card">
<h2>1 January & Islam</h2>
<p>
Aaj ka jo <b>1 January</b> hai,<br>
yeh <b>Islamic New Year nahi</b> hai.
</p>

<p>
Islam ka apna calendar hota hai —<br>
<b>Hijri calendar</b>, jo <b>Muharram</b> se shuru hota hai.
</p>

<p>
Isliye Muslims is din ko celebration ke taur par nahi manate.
</p>

<button class="btn" onclick="go('p3')">Next ↓</button>
</div>
</section>

<!-- PAGE 3 -->
<section id="p3">
<div class="card">
<h2>Qur’an & Sunnah ka Mafhoom</h2>
<p>
Qur’an me Allah batata hai ke<br>
<b>waqt aur saal Allah ke nizaam ka hissa hain</b><br>
(Qur’an 9:36 ka mafhoom).
</p>

<p>
Aur Rasoolullah ﷺ ne humein<br>
<b>non-Islamic festivals ko follow karne se mana</b> kiya hai.
</p>

<p>
Isliye hum na celebrate karte hain,<br>
na kisi ko bura bolte hain.
</p>

<button class="btn" onclick="go('p4')">Last ↓</button>
</div>
</section>

<!-- PAGE 4 -->
<section id="p4">
<div class="card">
<h2>Hum Kya Karte Hain?</h2>
<p>
Hum sirf:
</p>
<p>
• Allah ka shukr ada karte hain<br>
• Apni zindagi sudharne ki niyyat karte hain<br>
• Aur apni family ke liye dua 🤲
</p>

<p>
Allah hum sab ko imaan,<br>
sehat aur sukoon wali zindagi ata farmaye.
</p>

<h3>Ameen 🤍</h3>
</div>
</section>

<script>
function go(id){
document.getElementById(id).scrollIntoView({behavior:"smooth"});
}
</script>

</body>
</html>
