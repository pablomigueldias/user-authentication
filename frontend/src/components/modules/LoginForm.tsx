"use client";

import React, { useState } from "react"; 
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/Buttons"; 
import { Input } from "@/components/ui/Input";
import api from "@/services/api";

export function LoginForm() {
  const router = useRouter();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      const formData = new URLSearchParams();
      formData.append("username", email);
      formData.append("password", password);

      const response = await api.post("/auth/login", formData, {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      });

      const { access_token } = response.data;
      
      localStorage.setItem("token", access_token);
      
      router.push("/dashboard");

    } catch (err: any) {
      console.error(err);
      setError("Email ou senha incorretos. Tente novamente.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4 w-full max-w-sm">
      <div className="space-y-2">
        <h2 className="text-2xl font-bold tracking-tight text-center">Acesse sua conta</h2>
        <p className="text-sm text-slate-500 text-center">
          Entre com suas credenciais de administrador
        </p>
      </div>

      <div className="space-y-4 pt-4">
        <Input 
          label="Email" 
          type="email" 
          placeholder="admin@example.com"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        
        <Input 
          label="Senha" 
          type="password" 
          placeholder="******"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
      </div>

      {error && (
        <div className="p-3 text-sm text-red-500 bg-red-50 rounded-md border border-red-200">
          {error}
        </div>
      )}

      <Button type="submit" className="w-full" isLoading={loading}>
        Entrar no Sistema
      </Button>
    </form>
  );
}