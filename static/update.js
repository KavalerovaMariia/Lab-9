

function addProduct() {
    let Date = document.getElementById('date').value
    let steps = document.getElementById('steps').value
    fetch('/add', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'date': Date,
                             'steps': steps})
    })

}
function Clear() {
    fetch('/clear', {
        method: 'delete',
        headers: {'Content-Type': 'application/json'},

    })

}
