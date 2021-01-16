var grid = 37.39;
var gridOffset = grid / 20;
var secondClick = false;
var a, b;



function setup() {
    let cnv = createCanvas(300, 300);
    cnv.position(200,180);
    cnv.center('horizontal');

    background(255);0
    // Draw grid
    var l = 0;
    strokeWeight(1);
    stroke(151);
    while (l < width || l < height) {
        line(0, l, width, l);
        line(l, 0, l, height);
        l += grid;
    }
}

function draw() {
    strokeWeight(gridOffset);
    stroke(0, 0, 255);
    if (mouseIsPressed) {
      var x = snap(mouseX);
      var y = snap(mouseY);
      var px = snap(pmouseX);
      var py = snap(pmouseY);
      
      if (mouseButton == RIGHT){
        //background(250, 250, 150);
        //fill(15, 195, 185);
        erase();      
        line(px, py, x, y); 
        noErase();
      }
      else {
        line(px, py, x, y); 
      }
    }
  }
  
  
  function mouseClicked(){
    if (secondClick){
          secondClick = false;
          var x1 = snap(mouseX);
          var y1 = snap(mouseY);
          if (mouseButton == RIGHT){
            erase();
            line (a,b,x1,y1);
            noErase();
          }
          else {line (a,b,x1,y1);}
    }
    
    else {
      secondClick = true;
      a = snap(mouseX);
      b = snap(mouseY);
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