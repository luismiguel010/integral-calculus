import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import ttk
import threading
import time

class BezierCurveApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Curvas de Bézier Interactivas")
        
        # Variables
        self.num_points = 4
        self.control_points = []
        self.animation_running = False
        self.current_t = 0.0
        self.manual_t = 0.0
        self.t_step = 0.05
        
        # Crear interfaz
        self.setup_ui()
        self.setup_plot()
        self.generate_initial_points()
        
    def setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Frame de controles
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        
        # Control de número de puntos
        ttk.Label(control_frame, text="Número de puntos:").pack(side=tk.LEFT, padx=5)
        self.points_var = tk.IntVar(value=4)
        points_spinbox = ttk.Spinbox(control_frame, from_=2, to=10, width=5, 
                                   textvariable=self.points_var, command=self.update_points)
        points_spinbox.pack(side=tk.LEFT, padx=5)
        
        # Botones
        ttk.Button(control_frame, text="Generar Puntos", 
                  command=self.generate_initial_points).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Play", 
                  command=self.start_animation).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Stop", 
                  command=self.stop_animation).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Reset", 
                  command=self.reset_animation).pack(side=tk.LEFT, padx=5)
        
        # Frame para controles de t
        t_frame = ttk.Frame(main_frame)
        t_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        
        # Control manual de t
        ttk.Label(t_frame, text="Valor de t:").pack(side=tk.LEFT, padx=5)
        self.t_var = tk.DoubleVar(value=0.0)
        self.t_scale = ttk.Scale(t_frame, from_=0.0, to=1.0, orient=tk.HORIZONTAL,
                                variable=self.t_var, command=self.on_t_change)
        self.t_scale.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # Mostrar valor actual de t
        self.t_label = ttk.Label(t_frame, text="t = 0.00")
        self.t_label.pack(side=tk.LEFT, padx=5)
        
        # Botón para modo manual
        self.manual_mode = tk.BooleanVar(value=False)
        self.manual_check = ttk.Checkbutton(t_frame, text="Modo Manual", 
                                           variable=self.manual_mode,
                                           command=self.toggle_manual_mode)
        self.manual_check.pack(side=tk.LEFT, padx=5)
        
        # Frame para la gráfica
        self.plot_frame = ttk.Frame(main_frame)
        self.plot_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        
    def setup_plot(self):
        # Crear figura y subplot
        self.fig, self.ax = plt.subplots(figsize=(10, 8))
        self.ax.set_xlim(-1, 11)
        self.ax.set_ylim(-1, 11)
        self.ax.set_aspect('equal')
        self.ax.grid(True, alpha=0.3)
        self.ax.set_title("Curvas de Bézier Interactivas")
        
        # Canvas para tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Conectar eventos del mouse
        self.canvas.mpl_connect('button_press_event', self.on_click)
        self.canvas.mpl_connect('motion_notify_event', self.on_drag)
        self.canvas.mpl_connect('button_release_event', self.on_release)
        
        # Variables para arrastrar
        self.dragging = False
        self.drag_index = None
        
    def generate_initial_points(self):
        """Genera puntos de control iniciales"""
        self.num_points = self.points_var.get()
        self.control_points = []
        
        # Generar puntos en una línea diagonal
        for i in range(self.num_points):
            x = 2 + i * 2
            y = 2 + i * 1.5
            self.control_points.append([x, y])
        
        self.update_plot()
        
    def update_points(self):
        """Actualiza el número de puntos de control"""
        self.generate_initial_points()
        
    def bezier_curve(self, points, t):
        """Calcula la curva de Bézier para un valor de t"""
        if len(points) == 1:
            return points[0]
        
        # Algoritmo de De Casteljau
        new_points = []
        for i in range(len(points) - 1):
            x = (1 - t) * points[i][0] + t * points[i + 1][0]
            y = (1 - t) * points[i][1] + t * points[i + 1][1]
            new_points.append([x, y])
        
        return self.bezier_curve(new_points, t)
    
    def bezier_curve_full(self, points, num_samples=100):
        """Genera la curva completa de Bézier"""
        t_values = np.linspace(0, 1, num_samples)
        curve_points = []
        
        for t in t_values:
            point = self.bezier_curve(points, t)
            curve_points.append(point)
        
        return np.array(curve_points)
    
    def update_plot(self):
        """Actualiza la gráfica"""
        self.ax.clear()
        self.ax.set_xlim(-1, 11)
        self.ax.set_ylim(-1, 11)
        self.ax.set_aspect('equal')
        self.ax.grid(True, alpha=0.3)
        self.ax.set_title("Curvas de Bézier Interactivas")
        
        if len(self.control_points) >= 2:
            # Dibujar puntos de control
            control_x = [p[0] for p in self.control_points]
            control_y = [p[1] for p in self.control_points]
            
            # Puntos de control
            self.ax.scatter(control_x, control_y, c='red', s=100, zorder=5, 
                          picker=True, pickradius=10)
            
            # Líneas de control
            self.ax.plot(control_x, control_y, 'r--', alpha=0.5, linewidth=1)
            
            # Curva de Bézier completa
            if len(self.control_points) >= 2:
                curve = self.bezier_curve_full(self.control_points)
                self.ax.plot(curve[:, 0], curve[:, 1], 'b-', linewidth=2, 
                           label='Curva de Bézier')
            
            # Animación del punto actual
            display_t = self.current_t if self.animation_running else self.manual_t
            if 0 <= display_t <= 1:
                current_point = self.bezier_curve(self.control_points, display_t)
                self.ax.scatter(current_point[0], current_point[1], c='green', 
                              s=150, zorder=6, label=f't = {display_t:.2f}')
                
                # Mostrar construcción de la curva
                self.show_construction(display_t)
        
        self.ax.legend()
        self.canvas.draw()
        
    def show_construction(self, t):
        """Muestra la construcción de la curva para un valor de t"""
        if len(self.control_points) < 2:
            return
            
        # Algoritmo de De Casteljau visual
        current_points = self.control_points.copy()
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
        
        level = 0
        while len(current_points) > 1:
            next_points = []
            for i in range(len(current_points) - 1):
                x = (1 - t) * current_points[i][0] + t * current_points[i + 1][0]
                y = (1 - t) * current_points[i][1] + t * current_points[i + 1][1]
                next_points.append([x, y])
            
            # Dibujar líneas de construcción
            if len(current_points) > 1:
                x_coords = [p[0] for p in current_points]
                y_coords = [p[1] for p in current_points]
                color = colors[level % len(colors)]
                self.ax.plot(x_coords, y_coords, color=color, alpha=0.7, 
                           linewidth=2, linestyle='--')
            
            # Dibujar puntos intermedios
            if len(next_points) > 0:
                x_coords = [p[0] for p in next_points]
                y_coords = [p[1] for p in next_points]
                self.ax.scatter(x_coords, y_coords, c=color, s=50, alpha=0.8)
            
            current_points = next_points
            level += 1
    
    def on_click(self, event):
        """Maneja clics del mouse"""
        if event.inaxes != self.ax:
            return
        
        # Encontrar el punto más cercano
        min_dist = float('inf')
        closest_index = None
        
        for i, point in enumerate(self.control_points):
            dist = np.sqrt((event.xdata - point[0])**2 + (event.ydata - point[1])**2)
            if dist < min_dist and dist < 0.5:  # Radio de captura
                min_dist = dist
                closest_index = i
        
        if closest_index is not None:
            self.dragging = True
            self.drag_index = closest_index
    
    def on_drag(self, event):
        """Maneja el arrastre del mouse"""
        if not self.dragging or self.drag_index is None or event.inaxes != self.ax:
            return
        
        # Actualizar posición del punto
        self.control_points[self.drag_index] = [event.xdata, event.ydata]
        self.update_plot()
    
    def on_release(self, event):
        """Maneja la liberación del mouse"""
        self.dragging = False
        self.drag_index = None
    
    def start_animation(self):
        """Inicia la animación"""
        if not self.animation_running:
            self.animation_running = True
            self.animate_curve()
    
    def stop_animation(self):
        """Detiene la animación"""
        self.animation_running = False
    
    def reset_animation(self):
        """Reinicia la animación"""
        self.animation_running = False
        self.current_t = 0.0
        self.manual_t = 0.0
        self.t_var.set(0.0)
        self.update_plot()
    
    def on_t_change(self, value):
        """Maneja el cambio del slider de t"""
        self.manual_t = float(value)
        self.t_label.config(text=f"t = {self.manual_t:.2f}")
        if self.manual_mode.get():
            self.update_plot()
    
    def toggle_manual_mode(self):
        """Alterna entre modo manual y automático"""
        if self.manual_mode.get():
            self.stop_animation()
            self.update_plot()
        else:
            self.reset_animation()
    
    def animate_curve(self):
        """Anima la curva"""
        def animation_loop():
            while self.animation_running and self.current_t <= 1.0:
                self.current_t += self.t_step
                if self.current_t > 1.0:
                    self.current_t = 1.0
                
                self.update_plot()
                time.sleep(0.1)  # Control de velocidad
                
                if self.current_t >= 1.0:
                    self.animation_running = False
                    break
        
        # Ejecutar animación en un hilo separado
        animation_thread = threading.Thread(target=animation_loop)
        animation_thread.daemon = True
        animation_thread.start()

def main():
    root = tk.Tk()
    app = BezierCurveApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
