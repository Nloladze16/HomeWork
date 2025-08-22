var x = Number(window.prompt("შეიყვანეთ თქვენი ასაკი"));

if (x >= 18) {
  window.alert("თქვენ ხართ სრულწლოვანი");
} else if (x <= 0) {
  window.alert("თქვენ არ შეგიყვანიათ თქვენი ასაკი");
  console.log(x);
} else if (x < 18) {
  window.alert("თქვენ არ ხართ სრულწლოვანი");
} else {
  window.alert("თქვენ არ შეგიყვანიათ თქვენი ასაკი");
  console.log(x);
}

var result = (true && (false || true)) || (5 > 7 && 6 == 6) || (true && true);

document.writeln(result);
