function changecolor(x) {
 

  var color1 = Math.round(Math.random() * 255);
  var color2 = Math.round(Math.random() * 255);
  var color3 = Math.round(Math.random() * 255);

  var randomcolor = `rgb(${color1},${color2},${color3})`;

  x.style.backgroundColor = randomcolor
}
