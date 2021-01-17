var grid = 30; // # of tiles
var secondClick = false; // detect second click (might want to show indicator or smth)
var a, b; // previous/saved position
let lines = []; // array of lines
let button1, button2;

// storing json values ------------------------------------------------------------------
//let json = loadJSON('pointdata.json'); // load  JSON Object
let json = {};
var jsonArraySide = [];
var jsonArrayTop = [];
var jsonArrayFront = [];

// which grid we're in
var gridNum = 0;

function setup() {
  let cnv = createCanvas(1500, 500);
//  cnv.center('horizontal');
//  cnv.center('vertical');
  createGrid(); // forms grid
  //creating button
  button1 = createButton('Reset Canvases');
  button1.position(570, 650);
  button1.mousePressed(resetDraw);
  button2 = createButton('Submit');
  button2.position(873, 650);
  button2.mousePressed(submission);
}


function draw() { // update
  createGrid(); // clears grid
  drawLines(lines); // draw existing lines
}


function mouseClicked(){
    
  if (snap(mouseY) >= 30 && snap(mouseY) <= 390 && 
      ((snap(mouseX) >= 120 && snap(mouseX) <= 480) ||
       (snap(mouseX) >= 570 && snap(mouseX) <= 930) ||
       (snap(mouseX) >= 1020 && snap(mouseX) <= 1380))) {
    
    if (secondClick) { // if second click
      var x1 = snap(mouseX); // click position x
      var y1 = snap(mouseY); // click position y
      if (x1 != a || y1 != b) { // make sure not a point

        if (keyIsPressed == true && keyCode == CONTROL){ // delete func
          secondClick = false;

          removeLine(a, b, x1, y1, lines);
        }

        else {
          if (!containsLine(a, b, x1, y1, lines)) { // make sure line doesn't already exist
            secondClick = false;
            lines.push(new Edge(a, b, x1, y1)); // add line
          }
        }
      }
    }

    else {
      secondClick = true; // clicked first, prep second click
      a = snap(mouseX); // saves position x
      b = snap(mouseY); // saves position y
      //----------------------------------------------------------------------------------------------------------------
      if(a >= 120 && a <= 480) {
        gridNum = 1;
      }
      else if(a >= 570 && a <= 930) {
        gridNum = 2;
      }
      else {
        gridNum = 3;
      }
      
    }
  }
}

class Edge { // Line class
  constructor(coorx1, coory1, coorx2, coory2) {
    this.coorx1 = coorx1;
    this.coory1 = coory1;
    this.coorx2 = coorx2;
    this.coory2 = coory2;
  } 
}

function createGrid() {
  clear(); // wipes screen
  //background(255); // white background
  // Draw grid
  var l = 0;
  var count = 0;
  var border = 3;
  var bordera = 0;
  var sizeOfBox = 12;
  var desiredSpace=2;
  var mod = (sizeOfBox+desiredSpace);
  strokeWeight(1);
  stroke(50);
  while (l < width || l < height) {
    if (count>border){
      if (count<((width-(border*grid))/grid)) {   
        if (count <border+sizeOfBox+1 || (count!=17 && count!=18 && count!=32 && count!=33)){
            line(l, (bordera+1)*grid, l, ((bordera+1+sizeOfBox)*grid)); //vertical;
          }
      }
    }
    if (count!=0)
      if (count< (bordera+2+sizeOfBox)){ 
        for (let i=0; i<3; i++){
          line(((sizeOfBox*i)+(i+1)*border+1)*grid, l, ((sizeOfBox*(i+1)+border*(i+1)+1)*grid), l); //horizontal
        }
      }
    l += grid;
    count = count+1;
  }
}

function resetDraw() {
  secondClick = false;
  lines = [];
  createGrid();
}

function drawLines(lines) {
  stroke(0, 0, 255); // blue
  strokeWeight(3);
  for (let i = 0; i < lines.length; i++) { // draw the lines
    line(lines[i].coorx1, lines[i].coory1, lines[i].coorx2, lines[i].coory2);
    // ------------------------------------------------------------------------------------
    if(gridNum == 1) {
       if(!arrayIncludes(jsonArraySide, [lines[i].coorx1,lines[i].coory1]) 
          || JSON.stringify([lines[i].coory1,lines[i].coory1]) == JSON.stringify(jsonArraySide[0])) {
           jsonArraySide.push([lines[i].coorx1,lines[i].coory1]);  
       }
    }
    if(gridNum == 2) {
       if(!arrayIncludes(jsonArrayTop, [lines[i].coorx1,lines[i].coory1]) 
          || JSON.stringify([lines[i].coory1,lines[i].coory1]) == JSON.stringify(jsonArrayTop[0])) {
           jsonArrayTop.push([lines[i].coorx1,lines[i].coory1]);
       }
    }
    if(gridNum == 3) {
       if(!arrayIncludes(jsonArrayFront, [lines[i].coorx1,lines[i].coory1]) 
          || JSON.stringify([lines[i].coory1,lines[i].coory1]) == JSON.stringify(jsonArrayFront[0])) {
           jsonArrayFront.push([lines[i].coorx1,lines[i].coory1]);
       }
    }
  }
}

function snap(op) {
  // subtract offset (to center lines)
  // divide by grid to get row/column
  // round to snap to the closest one
  //var cell = Math.round((op - gridOffset) / grid);
  
  var cell = Math.round((op) / grid);
  
  // multiply back to grid scale
  // add offset to center
  //return cell * grid + gridOffset;
  
  return cell * grid ;
}

function removeLine(x1, y1, x2, y2, lines) { // remove line from array lines
  for (let i = 0; i < lines.length; i++) {
    if (doLinesMatch(x1, y1, x2, y2, lines[i])) {
      lines.splice(i, 1);
      if(gridNum == 1) {
        removeFromArray(jsonArraySide, [x1,y1]);
        removeFromArray(jsonArraySide, [x2,y2]);
      }
      if(gridNum == 2) {
        removeFromArray(jsonArrayTop, [x1,y1]);
        removeFromArray(jsonArrayTop, [x2,y2]);
      }
      if (gridNum == 3) {
        removeFromArray(jsonArrayFront, [x1,y1]);
        removeFromArray(jsonArrayFront, [x2,y2]);        
      }
    }
  }
}

function doLinesMatch(x1, y1, x2, y2, edge) { // checks if a line matches in lines array
  return (x1 == edge.coorx1 && y1 == edge.coory1 && x2 == edge.coorx2 && y2 == edge.coory2) ||
    (x1 == edge.coorx2 && y1 == edge.coory2 && x2 == edge.coorx1 && y2 == edge.coory1)
}

function containsLine(x1, y1, x2, y2, lines) { // checks if lines array contains line
  for (let i = 0; i < lines.length; i++) {
    if (doLinesMatch(x1, y1, x2, y2, lines)) {
      return true;
    }
  }
  return false;
}

// submit drawings to json file
function submission() {
  json.topView = jsonArrayTop;
  json.sideView = jsonArraySide;
  json.frontView = jsonArrayFront;
  // REMEMBER TO WRITE TO EXISTING JSON HERE ?? -----------------------------------------------------------
  saveJSON(json, 'pointdata.json');
  resetDraw();
}

// checks if 2d array contains an array
function arrayIncludes(array, element) {
  
  var stringElement = JSON.stringify(element);
  var stringArrayElement;
  
  for(var i = 0; i < array.length; i++) {
    
    stringArrayElement = JSON.stringify(array[i]);
    
    print(stringElement);
    print(stringArrayElement);
    
    if(stringElement == stringArrayElement) {
      return true;
    }
  }
  
  return false;
  
}

// remove from array
function removeFromArray(array, element) {
  
  var index = array.indexOf(element);
  array.splice(index, 1);
  return array;
  
}