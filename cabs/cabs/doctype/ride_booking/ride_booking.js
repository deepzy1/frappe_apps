frappe.ui.form.on('Ride Booking', {
	refresh(frm) {
		// your code here
	},

    rate(frm){
        frm.trigger("update_total_amount")
        
    },

    update_total_amount(frm){
        let total_distance=0;
        for (let item of frm.doc.items){
            total_distance+=item.distance;
        }

        const amount = frm.doc.rate * total_distance;
        frm.set_value("amount",amount)

    }
})

frappe.ui.form.on('Ride Booking Item', {
	refresh(frm) {
		// your code here
	},

    distance(frm,cdt,cdn){
        frm.trigger("update_total_amount")
        
    },
    items_remove(frm){

        frm.trigger("update_total_amount")
    },

    // distance(frm,cdt,cdn){
    //     console.log("distance changed");
    //     console.log(cdt)
    //     console.log(cdn)
    //     console.log(frappe.get_doc(cdt,cdn))

    //     my_child = frappe.get_doc(cdt,cdn)
    //     frappe.model.set_value(cdt,cdn,"source","Updated Source")
    // },

    

})

