import importlib
import pkgutil

from fastapi import APIRouter, FastAPI


def register_all_routes(app: FastAPI) -> None:
    import src.domains as domains_pkg

    print(f"Domains path: {domains_pkg.__path__}")
    for _, domain_name, is_pkg in pkgutil.iter_modules(domains_pkg.__path__):
        print(f"Found: {domain_name}, is_pkg: {is_pkg}")
        if not is_pkg:
            continue
        try:
            module = importlib.import_module(f"src.domains.{domain_name}.routes")
            router: APIRouter = module.router
            prefix = "" if domain_name == "ping" else f"/{domain_name}"
            app.include_router(router, prefix=prefix)
            print(f"Registered routes for domain: {domain_name} at {prefix or '/'}")
        except Exception as e:
            print(f"Failed to register routes for domain: {domain_name} — {e}")
