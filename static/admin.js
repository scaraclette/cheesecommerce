document.addEventListener('DOMContentLoaded', () => {
    console.log("hello");

    // Get current report for total purchases and total discounts given
    const reportRequest = new XMLHttpRequest();
    reportRequest.open('GET', '/admin/report');
    reportRequest.onload = () => {
        const data = JSON.parse(reportRequest.responseText);
        document.getElementById("currentReport").innerHTML = JSON.stringify(data);
        console.log(data);
    }
    reportRequest.send();


    // Calls the API to set new nth value and new discount code
    document.getElementById("setAll").onclick = () => {
        console.log("clicked button");
        let nVal = document.getElementById("nth").value;
        let codeVal = document.getElementById("disCode").value;

        if (nVal > 0 && codeVal != "") {
            let url = '/admin/set?n=' + nVal + '&code=' + codeVal;
            // console.log(url)

            const setRequest = new XMLHttpRequest();
            setRequest.open('POST', url);
            setRequest.onload = () => {
                const data = JSON.parse(setRequest.responseText);
                console.log(data);
                alert("new values set!");
            }

            setRequest.send();

        } else {
            alert("nth must be > 0 & code must have value!")
        }

    }
});