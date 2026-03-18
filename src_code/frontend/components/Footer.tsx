import Link from 'next/link';

const Footer = () => {
    return (
        <footer className="footer">
            <div className="footer-info">
                <p>&copy; 2024 Ecommerce</p>
                <ul>
                    <li><Link href="/about">About</Link></li>
                    <li><Link href="/contact">Contact</Link></li>
                    <li><Link href="/terms">Terms</Link></li>
                </ul>
            </div>
        </footer>
    );
};

export default Footer;