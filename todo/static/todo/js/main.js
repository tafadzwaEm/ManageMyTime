function realtimeClock(){

    var rtClock = new Date();

    var hours = rtClock.getHours();
    var minutes = rtClock.getMinutes();
    var seconds = rtClock.getSeconds();

    //Add AM and PM system
    var amPm = ( hours < 12 ) ? "AM" : "PM";

    //Convert the hours component to 12-hour format
    hours = (hours > 12) ? hours - 12 : hours;

    //Pad the hours, minutes and seconds with leading zeros
    hours = ("0" + hours).slice(-2);
    minutes = ("0" + minutes).slice(-2);
    seconds = ("0" + seconds).slice(-2);

    //display the clock
    document.getElementById('clock').innerHTML = hours + " : " + minutes + " : " + seconds + " " + amPm;

    var t = setTimeout(realtimeClock, 500);


    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = today.getFullYear();

    today = dd + '/' + mm + '/' + yyyy;

    //display date
    document.getElementById('todaysdate').innerHTML = "DATE: " + today
}
