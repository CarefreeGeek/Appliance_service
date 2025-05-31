document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    form.addEventListener("submit", function (e) {
        const name = document.getElementById("name");
        const address = document.getElementById("address");
        const phone = document.getElementById("phone");
        const applianceName = document.getElementsByName("appliance-name")[0];
        const problemType = document.getElementsByName("problem-type")[0];
        const serviceDate = document.getElementById("service-date");

        let isValid = true;
        let messages = [];

        // Name validation
        if (name.value.trim() === "") {
            isValid = false;
            messages.push("Name is required.");
        }

        // Address validation
        if (address.value.trim() === "") {
            isValid = false;
            messages.push("Address is required.");
        }

        // Phone validation (simple 10-digit number)
        const phoneRegex = /^[0-9]{10}$/;
        if (!phoneRegex.test(phone.value.trim())) {
            isValid = false;
            messages.push("Enter a valid 10-digit phone number.");
        }

        // Appliance name
        if (applianceName.value.trim() === "") {
            isValid = false;
            messages.push("Appliance name is required.");
        }

        // Problem type
        if (problemType.value.trim() === "") {
            isValid = false;
            messages.push("Appliance problem type is required.");
        }

        // Service date
        if (serviceDate.value === "") {
            isValid = false;
            messages.push("Service date is required.");
        } else {
            const today = new Date().toISOString().split("T")[0];
            if (serviceDate.value < today) {
                isValid = false;
                messages.push("Service date cannot be in the past.");
            }
        }

        if (!isValid) {
            e.preventDefault();
            alert("Please fix the following errors:\n\n" + messages.join("\n"));
        }
    });
});