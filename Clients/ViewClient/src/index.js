$('.datepicker').datepicker({
    format: 'yyyy-mm-dd',
    todayBtn: 'linked', 
    todayHighlight: true, 
    clearBtn: true,
});

$(document).ready(() => {
    getStatistics('');
});

$('#dateForm').submit(function(event) {
    event.preventDefault();
    
    date = document.getElementById('datepicker').value;
    getStatistics(date);
});

function toastSuccess(message) {
    $.toast({
        heading: 'Success',
        text: message,
        showHideTransition: 'slide',
        icon: 'success',
        hideAfter: 3500,
    });
}

function toastError(message) {
    $.toast({
        heading: 'Error',
        text: message,
        showHideTransition: 'slide',
        icon: 'error',
        hideAfter: 3500,
    });
}

var statistics = []

function getStatistics(date) {
    $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:8000/get_statistics/',
        dataType: 'json',
        data: {date: date},
        success: (response) => {
            statistics = response;
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
        var currentId = current['id'];

        var newRow = document.createElement('tr');
        newRow.id = `stat-${currentId}`;

        for(var key in current) {
            var newCell = document.createElement('td');
            newCell.id = `${key}-${currentId}`
            newCell.innerText = current[key];

            newRow.appendChild(newCell);
        }

        var editCell = document.createElement('button');
        editCell.setAttribute('class', 'btn btn-warning');
        editCell.setAttribute('onclick', `openModal("editModal", ${i})`);
        editCell.innerHTML = '<i class="fas fa-edit text-white"></i>';
        
        var newCell = document.createElement('td');
        newCell.appendChild(editCell)
        newRow.appendChild(newCell);

        var deleteCell = document.createElement('button');
        deleteCell.setAttribute('class', 'btn btn-danger');
        deleteCell.setAttribute('onclick', `deleteStat(${currentId})`);
        deleteCell.innerHTML = '<i class="fas fa-trash-alt"></i>';

        newCell = document.createElement('td');
        newCell.appendChild(deleteCell)
        newRow.appendChild(newCell);

        tableBody.appendChild(newRow);
    }
}

function deleteStat(statId) {
    if (confirm('Are you sure you want to delete this stat?')) {
        $.ajax({
            type: 'DELETE',
            url: `http://127.0.0.1:8000/delete/${statId}`,
            dataType: 'json',
            success: (response) => {
                toastSuccess(response.message);

                var rowElement = document.getElementById(`stat-${statId}`);
                rowElement.parentNode.removeChild(rowElement);
            },
            error: (response) => {
                toastError(response.responseJSON.message);
            },
        });
    }
}

function openModal(modalId, listPosition) {
    stat = statistics[listPosition];

    document.getElementById('statId').value = stat.id;
    document.getElementById('date').value = stat.date;
    document.getElementById('hour').value = stat.hour;
    document.getElementById('temperature').value = stat.temperature;
    
    var weatherOptions = document.getElementById('weather').getElementsByTagName('option')
    for (i = 0; i < weatherOptions.length; i++) {
        option = weatherOptions[i];
        
        if (option.innerText == stat.weather) {
            option.setAttribute('selected', true);
        } else {
            option.removeAttribute('selected');
        }
    }

    $(`#${modalId}`).modal('show');
}

$('#updateStatForm').on('submit', (event) => {
    event.preventDefault();
    const statId = document.getElementById('statId').value;
    const formData = new FormData(event.target);
    var data = Array.from(formData.entries()).reduce((memo, pair) => ({
        ...memo,
        [pair[0]]: pair[1],
    }), {});
    data = JSON.stringify(data);

    $.ajax({
        type: 'PUT',
        url: `http://127.0.0.1:8000/update/${statId}`,
        dataType: 'json',
        data: {
            statData: data,
        },
        success: (response) => {
            updateTableRowData(`stat-${statId}`, data);
            
            $(`#editModal`).modal('hide');
            toastSuccess(response.message);
        },
        error: (response) => {
            toastError(response.responseJSON.message);
        },
    });
});

function updateTableRowData(rowId, objData) {
    const element = document.getElementById(rowId);
    objData = JSON.parse(objData);

    for(let i = 1; i < element.children.length - 2; i++) {
        var currentChild = element.children[i];
        var key = currentChild.id.split('-')[0];
        
        currentChild.innerText = objData[key];  
    }
}