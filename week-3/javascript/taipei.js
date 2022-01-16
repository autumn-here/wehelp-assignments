// 串接api
let requestURL = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json';
let request = new XMLHttpRequest();
request.open('GET', requestURL);
request.send();
request.onload = function() {
  let data = JSON.parse(this.responseText);
  let attractionData = data['result']['results']
  // console.log(data);
  // console.log(attractionData);

  function getInfo(i){
     // 取得景點名稱
    // console.log(attractionData[i]['stitle'])
    let spotName = attractionData[i]['stitle']
    
    // 取得首圖網址
    let urls = attractionData[i]['file'].toLowerCase(); //轉小寫為確保切字串時，能取到第一個jpg檔案
    let urlIndex = urls.indexOf('.jpg')
    let coverUrl = urls.substr(0, (urlIndex+4))
    console.log(coverUrl)
    
    // 掛載圖片
    let spotImg = document.createElement("img");
    spotImg.setAttribute('src', coverUrl)
    document.querySelectorAll("figure")[i].appendChild(spotImg);

    // 掛載景點名稱
    let spotTitle = document.createElement('figcaption')
    spotTitle.textContent = spotName;
    document.querySelectorAll("figure")[i].appendChild(spotTitle);
  }

  //初始載入八張圖
  for(let i =0; i < 8; i++){
    getInfo(i)
  }

  //綁定button載入事件
  let loadBtn = document.getElementById('loadBtn');

  //建構新載入圖文的架構
  function createFigure(){
    let figure = document.createElement('figure');
    document.getElementById('gallery').appendChild(figure);
  }

  //紀錄載入次數，藉此對照載入json資料
  let loadCount = 8

  loadBtn.addEventListener(
    "click",
    function(){
      console.log("click event")
      for (let i = loadCount; i < (loadCount+8) && i < 58; i++) {
        createFigure()
        getInfo(i)
      }

      //JSON檔案資料總共58筆，當載入超過此數量則提示沒有更多資料
      if (loadCount >= 58){
        alertLast()
        return
      }

      //紀錄載入次數
      loadCount += 8
    }
  )
  function alertLast(){
    alert('沒有更多內容了')
  }
  }