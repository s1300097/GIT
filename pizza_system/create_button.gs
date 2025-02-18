const sheet = SpreadsheetApp.getActiveSheet();
function create() {
  const amount = sheet.getRange("A3").getValue();
  const last = sheet.getLastRow();
  let sum = 2000;
  if (last != 6){
    sum = sheet.getRange(last, 1).getValue();
  }
  if(amount != 0){
    sheet.getRange(last +1, 1, 1, 4).setValues([[sum +1, amount, "---", 0]]);
  }
}