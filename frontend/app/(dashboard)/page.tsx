export default function DashboardPage() {
  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
          <h1 className="text-3xl font-bold text-gray-900">Dashboard</h1>
        </div>
      </header>
      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <div className="px-4 py-6 sm:px-0">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div className="bg-white overflow-hidden shadow rounded-lg p-6">
              <h2 className="text-lg font-medium text-gray-900">Portfolio Value</h2>
              <p className="mt-2 text-3xl font-bold text-gray-900">$0.00</p>
            </div>
            <div className="bg-white overflow-hidden shadow rounded-lg p-6">
              <h2 className="text-lg font-medium text-gray-900">Total Return</h2>
              <p className="mt-2 text-3xl font-bold text-green-600">+0.00%</p>
            </div>
            <div className="bg-white overflow-hidden shadow rounded-lg p-6">
              <h2 className="text-lg font-medium text-gray-900">Assets</h2>
              <p className="mt-2 text-3xl font-bold text-gray-900">0</p>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
