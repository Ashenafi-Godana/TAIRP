function fun1() {
  var fnum = document.getElementById("txt1").value;
  var snum = document.getElementById("txt2").value;

  var tot = parseInt(fnum) + parseInt(snum);

  document.getElementById("result").innerHTML = tot;
}
