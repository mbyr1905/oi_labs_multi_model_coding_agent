import type { NextPage, GetServerSideProps } from 'next';
import { useState, useEffect } from 'react';
import { api } from '../lib/api';

interface Product {
    id: number;
    name: string;
    price: number;
    description: string;
}

const ProductPage: NextPage<{ product: Product }> = ({ product }) => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

    return (
        <>
            <h1>{product.name}</h1>
            <p>{product.description}</p>
            <p>Price: {product.price}</p>
        </>
    );
};

export const getServerSideProps: GetServerSideProps = async (context) => {
    const id = context.params.id;
    const response = await api(`products/${id}`);
    const product = response;

    return {
        props: {
            product,
        },
    };
};

export default ProductPage;