function update() {
  const sheet = SpreadsheetApp.getActiveSheet();
  sheet.getRange("D4").setValue("");
  const id = sheet.getRange("D3").getValue();

  const data = sheet.getRange(7, 1, sheet.getLastRow() -6, 1).getValues(); //[ [ 1001 ], [ 1002 ], [ 1003 ], [ 1004 ] ]
  const length = data.length;
  let result = -1;
  for (var i = 0; i < length; i++){
    if (id == data[i][0]){
      result = i;
      break;
    }
  }

  const range = sheet.getRange(result +7, 3, 1, 3);
  const array = range.getValues();

  if (result == -1 || array[0][1] == 1){
    console.error();
    sheet.getRange("D4").setValue("ERROR!!");
  }
  else{
    const userID = sheet.getRange(result +7, 3).getValue();
    let message = 'ご注文の商品が完成しました！\n店頭までお越しください\nID: ' + sheet.getRange(result +7, 1).getValue();
    if(array[0][0] != "---"){
      lineReply(message, userID);
    }
    range.setValues([["---", 1, time()]]);
    const next = sheet.getRange(result +8, 1).getValue();
    sheet.getRange("D3").setValue(next);
  }
}

function time(){
  const now = new Date();
  const HourValue = now.getHours();
  const MinValue = now.getMinutes();
  const SecValue = now.getSeconds();
  const time = HourValue + ":" + ('00' + MinValue).slice(-2) + ":" + ('00' + SecValue).slice(-2);
  return time;
}