// LINE developersのメッセージ送受信設定に記載のアクセストークン
const LINE_TOKEN = 'D8eCa7BjGsNKFJz5zQSejx7SQxNCtsZ6A8X3yb1fj3cd3nKnVLDcAnAvF23QpZo6aD960WIasAxisYN2EsDbNnoxhE7Qtbk63JipFUo8PAR1qiVYZD6FiwJq2fdsnx9mJg2uWyPF8886h52BQF6wSAdB04t89/1O/w1cDnyilFU='; // Messaging API設定の一番下で発行できるLINE Botのアクセストークン（Channel Secretはいらないみたいです。）
const LINE_URL = 'https://api.line.me/v2/bot/message/reply';
const LINE_ENDPOINT = 'https://api.line.me/v2/bot/message/push';

//postリクエストを受取ったときに発火する関数
function doPost(e) {
  
  let replyToken;
  let userID;
  let userMessage;
  let msg;
  try{
    // 応答用Tokenを取得
    replyToken = JSON.parse(e.postData.contents).events[0].replyToken;
    // 記録用userIDを取得
    userID = JSON.parse(e.postData.contents).events[0].source.userId;
    // メッセージを取得
    userMessage = JSON.parse(e.postData.contents).events[0].message.text;
    // メッセージを改行ごとに分割
    msg = userMessage.replaceAll("　", " ").split(" ");
  }
  catch(e){
    console.log(e.message);
    return;
  }
  
  // 返答用メッセージを作成
  const messages = [];
  
  // スプシとの連携開始
  const sheet = SpreadsheetApp.getActiveSheet();
  const data = sheet.getRange(7, 1, sheet.getLastRow() -6, 1).getValues(); //[ [ 1001 ], [ 1002 ], [ 1003 ], [ 1004 ] ]
  const length = data.length;
  let result = -1;
  for (var i = 0; i < length; i++){  // 入力されたIDが存在するか
    if (msg[0] == data[i][0]){
      result = i;
      break;
    }
  }
  const range = sheet.getRange(result +7, 3); // address
  const user = range.getValue();  // value
  let after_msg = {};

  if(result != -1 && msg[1] == "確認"){
    const flag = sheet.getRange(result +7, 4).getValue();
    after_msg = {
    'type': 'text',
    'text': check(flag),
    }
  }
  else if (result != -1 && user == "---" && sheet.getRange(result +7, 4).getValue() == 0){
  // 返答用メッセージを追加
    after_msg = {
    'type': 'text',
    'text': "確認しました",
    }
    // userIDの記録
    range.setValue(userID);
  }
  else{
    after_msg = {
    'type': 'text',
    'text': "受け付けできません",
    }
  }
  messages.push(after_msg);
  
  // lineで返答する
  UrlFetchApp.fetch(LINE_URL, {
    'headers': {
      'Content-Type': 'application/json; charset=UTF-8',
      'Authorization': `Bearer ${LINE_TOKEN}`,
    },
    'method': 'post',
    'payload': JSON.stringify({
      'replyToken': replyToken,
      'messages': messages,
    }),
  });
  
  ContentService.createTextOutput(JSON.stringify({'content': 'post ok'})).setMimeType(ContentService.MimeType.JSON);  
}

// メッセージに「確認」が付与されたときに使用
function check(flag){
  //const test = sheet.getRange("D7").getValue();
  let c_msg = "";
  if(flag == 0){
    c_msg = "すみません！\nまだ完成しておりません";
  }
  else if(flag == 1){
    c_msg = "すでに完成してます\nまだ受け取られていない場合は、店頭までお越しください";
  }
  return c_msg;
}

// 通知送信用
function lineReply(replyText, LINE_USERID) {
  const headers = {
    "Authorization": "Bearer " + LINE_TOKEN,
    'Content-type': 'application/json'
  }
  const messages = {
    "headers": headers,
    "to": LINE_USERID,
    "messages": [{
      "type": "text",
      "text": replyText
    }]
  };
  const options = {
    "headers": headers,
    "payload": JSON.stringify(messages)
  };

  UrlFetchApp.fetch(LINE_ENDPOINT, options);
}