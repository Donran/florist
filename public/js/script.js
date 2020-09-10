const MONTHS_TO_NUM = {
    "januari": 0,
    "februari": 1,
    "mars": 2,
    "april": 3,
    "maj": 4,
    "juni": 5,
    "juli": 6,
    "augusti": 7,
    "september": 8,
    "oktober": 9,
    "november": 10,
    "december": 11
}

const closed_days = [
    "Nyårsdagen: 1 januari",
    "Trettondedag jul: 6 januari",
    "Första maj: 1 maj",
    "Sveriges nationaldag: 6 juni",
    "Julafton: 24 december",
    "Juldagen: 25 december",
    "Annandag jul: 26 december",
    "Nyårsafton: 31 december"
];
function closedDays()
{
    let today=new Date();
    let one_day=10006060*24;
    let sorted_days = []


    let closed_days_dates = closed_days.map(day => {
        let day_arr = day.split(" ");
        let month = MONTHS_TO_NUM[day_arr.pop()];
        let date = parseInt(day_arr.pop());
        let year = today.getMonth() > month ? today.getFullYear() + 1 : today.getFullYear()

        return {day: day, date: new Date(year, month, date)};
    });

    let days_and_days_diff = closed_days_dates.map(closedDate => {
        let days_diff = Math.ceil((closedDate.date.getTime()-today.getTime())/(one_day))
        return [days_diff, closedDate.day]
    });

    sorted_days = days_and_days_diff.sort(sortByFirstColumn);

    function sortByFirstColumn(a, b) {
        if (a[0] === b[0]) {
            return 0;
        }
        else {
            return (a[0] < b[0]) ? -1 : 1;
        }
    }
    return sorted_days;
}


$(document).ready(() => {
    if(window.location.pathname.toLowerCase() == "/hitta_hit.html") {
        days = closedDays();
        days.forEach(day => {
            console.log(day);
            $("#closed-days").append(`<li class="closed-day">${day[1]}</li>`);
        });
    }
});
