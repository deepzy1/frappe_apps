import { Button, Card } from '@frappe/ui';

export default function WebPage() {
    return (
        <div>
            <Card title="Welcome to Cabs">
                <p>This is a sample webpage using Frappe UI components.</p>
                <Button onClick={() => frappe.msgprint("Hello from Cabs!")}>
                    Click Me
                </Button>
            </Card>
        </div>
    );
}
