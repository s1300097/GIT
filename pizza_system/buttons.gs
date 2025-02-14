//Inventory Management

//const sheet = SpreadsheetApp.getActiveSheet();
const b1 = sheet.getRange("H5");
const b2 = sheet.getRange("J5");

function button1() {//H7
  const h = b1.getValue();
  b1.setValue(h-1);
}

function button2() {///J7
  const j = b2.getValue();
  b2.setValue(j-1);
}

function reset() {
  b1.setValue(50);
  b2.setValue(12);
}