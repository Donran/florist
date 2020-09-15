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

function sortByFirstColumn(a, b) {
    if (a[0] === b[0]) {
        return 0;
    }
    else {
        return (a[0] < b[0]) ? -1 : 1;
    }
}
function checkZipcode()
{
    let blommogram = $(".blommogram");
    let zippies = [
        "98138",
        "98139",
        "98140",
        "98142",
    ];
    let zip = $("#zipcode").val().replace(/[\s\D-]/gi, "");

    blommogram.popover('enable');
    setTimeout(() => {
        blommogram.popover('hide');
        blommogram.popover('disable');
    }, 3000);
    if (zippies.includes(zip)) {
        blommogram.attr("data-content", "Vi skickar blommor inom detta postnummer.");
    } else {
        blommogram.attr("data-content", "Vi skickar inte blommor inom detta postnummer.");
    }

    blommogram.popover('show');

}
/**
 * Gets closed days from hitta_hit.html.
 * Then sorts them by closest date.
 */
function getClosedDays()
{
    let closedDays = [];
    let closedDaysHTML = document.getElementsByClassName("closed-day");
    for(let i = 0; i < closedDaysHTML.length; i++){
        let children = closedDaysHTML[i].children
        let closedDay = children[0].innerHTML + ": " + children[1].innerHTML
        closedDays.push(closedDay)
    }

    let today=new Date();
    let oneDay=1000*60*60*24;

    let closedDaysDates = closedDays.map(day => {
        let dayArr = day.split(" ");
        let month = MONTHS_TO_NUM[dayArr.pop()];
        let date = parseInt(dayArr.pop());
        let year = today.getFullYear()

        if(month < today.getMonth()){
            year+=1
        } else if(month == today.getMonth()) {
            if(date < today.getDate()) {
                year+=1
            }
        }

        return {day: day, date: new Date(year, month, date)};
    });

    let sortedDays = closedDaysDates.map(closedDate => {
        let daysDiff = Math.ceil((closedDate.date.getTime()-today.getTime())/(oneDay))
        return [daysDiff, closedDate.day]
    }).sort(sortByFirstColumn);

    return sortedDays;
}

function updateClosedDays() {

    days = getClosedDays();
    $("#closed-days-tbody").html("");
    days.forEach(day => {
        day = day[1].split(":")
        $("#closed-days-tbody").append(`<tr class="closed-day"><td>${day[0]}</td><td>${day[1]}</td></tr>`)
    });
}


$(document).ready(() => {
    let fileName = window.location.pathname.toLowerCase();
    fileName = fileName.split("/");
    fileName = fileName[fileName.length-1];
    if(fileName == "hitta_hit.html") {
        // Remove the class .onlyjs from map to make it visible
        $("#map").removeClass("onlyjs");
        updateClosedDays();
    } else if(fileName == "index.html" || fileName == "") {
        $('.blommogram').popover();
        $('.blommogram').popover("disable");
    }
});
