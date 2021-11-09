$('#datepicker').datepicker({
    format: 'yyyy-mm-dd',
    todayBtn: true, 
});

$(document).ready(() => {
    getStatistics('');
});

$('#dateForm').submit(function(event) {
    event.preventDefault();
    
    date = document.getElementById('datepicker').value;
    getStatistics(date);
});

function getStatistics(date) {
    $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:8000/get_statistics/',
        dataType: 'json',
        data: {date: date},
        success: (response) => {
            console.log(response);
        },
        error: (response) => {
            console.log(`Error => ${response}`);
        }     
    });
}