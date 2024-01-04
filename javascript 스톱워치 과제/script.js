const record = document.getElementById("record");
const timer = document.getElementById("timer");
// const recordbox = document.getElementById("record");
const remove = document.getElementsByClassName("fa-trash");

//시간 저장할 변수 선언
let time = 0;
let timeflow = false;
let sec, msec;

//시작할때 시작 시간을 출력하도록 설정
timenow();

//이벤트발생(start,stop,reset등) 시에 시간을 업데이트 하는 함수
function timenow() {
  timer.innerText = getTime();
  if (timeflow) {
    time++;
    return setTimeout(timenow, 10);
  }
}

//ms로된 시간을 보기 편하도록 바꿔주는 함수
function getTime() {
  sec = fillZero(String(Math.floor(time / 100)));
  msec = fillZero(time % 100);

  return sec + ":" + msec;
}

//두자리수로 만들어주는 함수
function fillZero(num) {
  return String(num).padStart(2, "0");
}

// start 버튼
function start() {
  timeflow = true;
  timenow();
}

//stop 버튼
function stop() {
  timeflow = false;
  timenow();

  const recordstop = document.createElement("div");
  recordstop.classList.add("record");
  const img1 = document.createElement("i");
  const img2 = document.createElement("div");
  img1.classList.add("fa-regular", "fa-circle");
  // img2.classList.add("fa-solid", "fa-trash");

  recordstop.append(img1, getTime(), img2);
  record.appendChild(recordstop);
}

// 초기화 버튼
function reset() {
  time = 0;
  sec = 0;
  msec = 0;
  timeflow = false;
  timenow();
}

//체크박스
record.addEventListener("click", (e) => {
  //체크하기
  if (e.target.className === "fa-regular fa-circle main checked") {
    const checked = document.getElementsByClassName("fa-regular");
    e.target.classList.toggle("checked");
    for (let k of checked) {
      if (k.className === "fa-regular fa-circle checked") {
        k.classList.toggle("checked");
      }
    }
  } else if (e.target.className === "fa-regular fa-circle main") {
    const checked = document.getElementsByClassName("fa-regular");
    e.target.classList.toggle("checked");
    for (let k of checked) {
      if (k.className === "fa-regular fa-circle") {
        k.classList.toggle("checked");
      }
    }
  } else if (
    e.target.className === "fa-regular fa-circle" ||
    e.target.className === "fa-regular fa-circle checked"
  ) {
    e.target.classList.toggle("checked");

    // 전체 선택되었을 경우 main도 체크해주기
    const target = document.getElementsByClassName("checked");
    const all = document.getElementsByClassName("fa-regular");
    if (target.length === all.length - 1) {
      all[0].classList.toggle("checked");
    }
  }

  //삭제버튼
  if (e.target.className === "fa-solid fa-trash") {
    const checked = document.getElementsByClassName("checked");
    let len = checked.length;
    let cnt = 0;
    for (let j = 0; j < len; j++) {
      if (checked[cnt].parentElement.className == "record") {
        record.removeChild(checked[cnt].parentElement);
      } else {
        cnt++;
      }
    }
  }
});
