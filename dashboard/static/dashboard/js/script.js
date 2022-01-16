function deleteEntryBySNO(id) {
    let confirmation = confirm("Do you want to delete the selected item. This action is can't be reversed.");
    if (confirmation == true) {
        let item = document.getElementById(id);
        let redirect = item.getAttribute('data-bs-debitCredit');
        let dataID = item.getAttribute("data-bs-id");
        window.location = `/dashboard/Ledger/Delete/BySNO/${dataID}/?redirect=${redirect}`;
    }
};

function updateEntry(id) {
    let item = document.getElementById(id);
    let redirect = item.getAttribute('data-bs-debitCredit');
    let dataID = item.getAttribute("data-bs-id");
    window.location = `/dashboard/Ledger/Update/${dataID}/?redirect=${redirect}`;
};

function readEntry(id) {
    let item = document.getElementById(id);
    let redirect = item.getAttribute('data-bs-debitCredit');
    let dataID = item.getAttribute("data-bs-id");
    window.location = `/dashboard/Ledger/Update/${dataID}/?redirect=${redirect}`;
};