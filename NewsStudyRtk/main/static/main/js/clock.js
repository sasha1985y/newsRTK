setInterval(() => {
  let hours = document.getElementById('hours');
  let minutes = document.getElementById('minutes');
  let seconds = document.getElementById('seconds');
  let amPm = document.getElementById('ampm');

  let hh = document.getElementById('hh');
  let mm = document.getElementById('mm');
  let ss = document.getElementById('ss');

  let h = new Date().getHours();
  let m = new Date().getMinutes();
  let s = new Date().getSeconds();
  let am = h >= 12 ? 'PM' : 'AM';

  if (h > 12) {
    h = h - 12;
  }

  h = (h < 10) ? '0' + h : h;
  m = (m < 10) ? '0' + m : m;
  s = (s < 10) ? '0' + s : s;

  hours.innerHTML = h + "<br><br><span>Hours</span></br></br>";
  minutes.innerHTML = m + "<br><br><span>Minutes</span></br></br>";
  seconds.innerHTML = s + "<br><br><span>Seconds</span></br></br>";
  amPm.innerHTML = am;

  hh.style.strokeDashoffset = 250 - (250 * h) / 12;
  mm.style.strokeDashoffset = 250 - (250 * m) / 60;
  ss.style.strokeDashoffset = 250 - (250 * s) / 60;

})