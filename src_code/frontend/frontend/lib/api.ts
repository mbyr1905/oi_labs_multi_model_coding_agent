export const api = async (endpoint: string, method: string = 'GET', data?: any) => {
    try {
        const response = await fetch(`http://localhost:8000/${endpoint}`, {
            method,
            headers: {
                'Content-Type': 'application/json'
            },
            body: data ? JSON.stringify(data) : null
        });
        if (!response.ok) {
            throw new Error(response.statusText);
        }
        return await response.json();
    } catch (error) {
        console.error(error);
        throw error;
    }
};