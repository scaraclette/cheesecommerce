document.addEventListener('DOMContentLoaded', () => {

    document.getElementById("buyMore").onclick = () => {
        const buyRequest = new XMLHttpRequest();
        buyRequest.open('POST', '/customer/buy/');
        buyRequest.onload = () => {
            const data = JSON.parse(buyRequest.responseText);
            alert(JSON.stringify(data))
        }
        buyRequest.send();
    }

});