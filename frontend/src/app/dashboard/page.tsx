"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import api from "@/services/api.js";
import { Button } from "@/components/ui/Buttons";


interface User {
  id: string;
  email: string;
  username: string;
}

export default function Dashboard() {
  const router = useRouter();
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    api.get("/users/me")
      .then((response) => {
        setUser(response.data);
      })
      .catch(() => {
        router.push("/");
      });
  }, [router]);

  function handleLogout() {
    localStorage.removeItem("token");
    router.push("/");
  }

  if (!user) return <div className="p-8 text-center">Carregando dados seguros...</div>;

  return (
    <div className="min-h-screen bg-white p-8">
      <div className="max-w-4xl mx-auto">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-3xl font-bold text-slate-900">Dashboard Seguro 🔐</h1>
          <Button variant="outline" onClick={handleLogout}>Sair</Button>
        </div>

        <div className="bg-slate-50 p-6 rounded-lg border border-slate-200">
          <h2 className="text-xl font-semibold mb-4">Bem-vindo, {user.username}!</h2>
          <p className="text-slate-600">
            Se você está vendo isso, seu Token JWT foi validado com sucesso pelo Backend.
          </p>
          <div className="mt-4 p-4 bg-white rounded border border-slate-200 font-mono text-sm">
            <p><strong>ID:</strong> {user.id}</p>
            <p><strong>Email:</strong> {user.email}</p>
          </div>
        </div>
      </div>
    </div>
  );
}