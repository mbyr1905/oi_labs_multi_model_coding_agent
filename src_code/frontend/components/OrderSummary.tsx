import { useState } from 'react';

const OrderSummary = ({ products }) => {
    const [subtotal, setSubtotal] = useState(0);
    const [tax, setTax] = useState(0);
    const [total, setTotal] = useState(0);

    const calculateSubtotal = () => {
        let subtotal = 0;
        products.forEach((product) => {
            subtotal += product.price;
        });
        setSubtotal(subtotal);
    };

    const calculateTax = () => {
        const taxRate = 0.08;
        setTax(subtotal * taxRate);
    };

    const calculateTotal = () => {
        setTotal(subtotal + tax);
    };

    calculateSubtotal();
    calculateTax();
    calculateTotal();

    return (
        <div className="order-summary">
            <h2>Order Summary</h2>
            <p>Subtotal: ${subtotal}</p>
            <p>Tax (8%): ${tax}</p>
            <p>Total: ${total}</p>
        </div>
    );
};

export default OrderSummary;