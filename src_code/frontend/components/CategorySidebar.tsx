import Link from 'next/link';

const CategorySidebar = () => {
    return (
        <div className="category-sidebar">
            <h2>Categories</h2>
            <ul>
                <li><Link href="/products?category=electronics">Electronics</Link></li>
                <li><Link href="/products?category=fashion">Fashion</Link></li>
                <li><Link href="/products?category=home">Home</Link></li>
            </ul>
        </div>
    );
};

export default CategorySidebar;