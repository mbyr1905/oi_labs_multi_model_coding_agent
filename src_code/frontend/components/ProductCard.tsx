import Link from 'next/link';

const ProductCard = ({ product }) => {
    return (
        <div className="product-card">
            <Link href={`/products/${product.id}`}> 
                <img src={product.image} alt={product.title} />
            </Link>
            <div className="product-info">
                <h2>{product.title}</h2>
                <p>{product.description}</p>
                <p>${product.price}</p>
            </div>
        </div>
    );
};

export default ProductCard;