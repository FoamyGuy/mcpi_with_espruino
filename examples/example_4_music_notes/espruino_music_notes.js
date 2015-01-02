// map to hold the frequency of each note.
var notes = { "c3": 130.81,
              "d3": 146.83,
              "e3": 164.81,
              "f3": 174.61,
              "g3": 196.00,
              "a3": 220.00,
              "b3": 246.94,
              "c4": 261.63,
              "d4": 293.66,
              "e4": 329.63,
              "f4": 349.23,
              "g4": 392.00,
              "a4": 440.00,
              "b4": 493.88,
              "c5": 523.25,
              "d5": 587.33,
              "e5": 659.25,
              "f5": 698.46,
              "g5": 783.99,
              "a5": 880.00,
              "b5": 987.77};

// optional scale array to represent two full octaves.
var scale = ['c4', 'd4', 'e4', 'f4', 'g4', 'a4', 'b4',
             'c5', 'd5', 'e5', 'f5', 'g5', 'a5', 'b5'];

// call this method and pass it a note i.e. 'c4' to have it play.
function playNote(note){
  print("playing note: " + note);
  analogWrite(A0, 0.5, {freq: notes[note]});
  var startTime = getTime();
  var endTime = startTime + 0.1;
  while(getTime() < endTime){
    // It's terrible, I know.
    // But using setTimeout() made the code
    // a lot harder to understand. Please forgive me.
  }
}

// rest (silence) you can optionally pass it how long to rest  in seconds.
function rest(time){
  analogWrite(A0, 0);
  var endTime = getTime() + time;
  while(getTime() < endTime){
    // It's terrible, I know.
    // But using setTimeout() made the code
    // a lot harder to understand. Please forgive me.
  }
}

// Test function that playes the two octave scale up and then down.
function playScale(){
  var i = 0;
  while (i < scale.length){
    playNote(scale[i]);
    rest(0.05);
    i++;
  }
  i -= 2;
  while (i >= 0){
    playNote(scale[i]);
    rest(0.05);
    i--;
  }
  analogWrite(A0, 0);
}

//Uncomment to test:
playScale();
