frappe.ui.form.on("Ride Order",{
    onload(frm){
        console.log("running onload");

    },

    setup(frm){
        console.log("Running setup");

    },
    refresh(frm){
        console.log("Refresh")
        if (frm.doc.status !== "Accepted"){
            frm.add_custom_button("Accept",() =>{
            // frappe.show_alert("Button is working")

            frm.set_value("status","Accepted");
            frm.save()
        },"Actions")

        frm.add_custom_button("Reject",()=>{
            frm.set_value("status","Rejected");
            frm.save()

        },"Actions")
        }

        

       

    },
});