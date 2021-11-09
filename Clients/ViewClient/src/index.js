$('#datepicker').datepicker({
    format: 'yyyy-mm-dd',
    todayBtn: true, 
    todayHighlight: true, 
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
            putOnTable(response);
        },
        error: (response) => {
            console.log(`Error => ${response}`);
        }     
    });
}

function putOnTable(statistics) {
    $('#statisticsTable tbody tr').remove();
    
    var tableBody = document.getElementById('statisticsTableBody');

    for(i = 0; i < statistics.length; i++) {
        var current = statistics[i];
        var newRow = document.createElement('tr');

        for(var key in current) {
            var newCell = document.createElement('td');
            newCell.innerText = current[key];

            newRow.appendChild(newCell);
        }

        var editCell = document.createElement('button');
        editCell.setAttribute('class', 'btn btn-warning');
        editCell.innerHTML = '<i class="fas fa-edit text-white"></i>';
        var newCell = document.createElement('td');
        newCell.appendChild(editCell)
        newRow.appendChild(newCell);

        var deleteCell = document.createElement('button');
        deleteCell.setAttribute('class', 'btn btn-danger');
        deleteCell.innerHTML = '<i class="fas fa-trash-alt"></i>';
        var newCell = document.createElement('td');
        newCell.appendChild(deleteCell)
        newRow.appendChild(newCell);

        tableBody.appendChild(newRow);
    }
}