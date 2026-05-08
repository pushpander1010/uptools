# UpTools Quick Reference - Breadcrumbs & Mobile Menu

## TL;DR - Add to Every Tool Page

### 1. Update Import (Line ~839)
```javascript
import { ..., createBreadcrumb, initMobileMenu } from '/scripts/utils.js';
```

### 2. Add at End of Script
```javascript
createBreadcrumb([
  { label: 'Home', href: '/' },
  { label: 'Category', href: '/#category' },
  { label: 'Tool Name' }
]);
initMobileMenu();
```

---

## Category Reference

| Category | Href |
|----------|------|
| Finance | `/#finance` |
| Tax | `/#tax` |
| Banking | `/#banking` |
| Crypto | `/#crypto` |
| Images | `/#images` |
| Text | `/#text` |
| Developer | `/#dev` |
| Security | `/#security` |
| Networking | `/#networking` |
| Health | `/#health` |
| Canada | `/#canada` |
| Social | `/#social` |
| AI | `/#ai` |
| Marketing | `/#marketing` |
| Fun | `/#fun` |

---

## Examples

### BMI Calculator
```javascript
createBreadcrumb([
  { label: 'Home', href: '/' },
  { label: 'Health', href: '/#health' },
  { label: 'BMI Calculator' }
]);
initMobileMenu();
```

### Income Tax Tool
```javascript
createBreadcrumb([
  { label: 'Home', href: '/' },
  { label: 'Tax', href: '/#tax' },
  { label: 'Income Tax Calculator' }
]);
initMobileMenu();
```

### AI Writer
```javascript
createBreadcrumb([
  { label: 'Home', href: '/' },
  { label: 'AI', href: '/#ai' },
  { label: 'AI Writing Assistant' }
]);
initMobileMenu();
```

### Snake Game
```javascript
createBreadcrumb([
  { label: 'Home', href: '/' },
  { label: 'Games', href: '/games/' },
  { label: 'Snake' }
]);
initMobileMenu();
```

---

## Batch Update All Tools

```bash
node scripts/batch-add-breadcrumbs.mjs
```

---

## Testing

### Desktop
- [ ] Breadcrumb visible
- [ ] Links work
- [ ] Mobile menu hidden

### Mobile
- [ ] Breadcrumb visible
- [ ] Mobile menu appears
- [ ] Menu opens/closes
- [ ] Links work

---

## CSS Classes

- `.breadcrumb` - Main nav
- `.breadcrumb-list` - List
- `.breadcrumb-item` - Item
- `.mobile-menu-toggle` - Hamburger button
- `.nav-links` - Navigation
- `.nav-links.active` - Active menu

---

## Troubleshooting

**Breadcrumb not showing?**
- Check `<main>` element exists
- Verify `createBreadcrumb()` is called
- Check browser console for errors

**Mobile menu not working?**
- Verify `.mobile-menu-toggle` button exists
- Check `.nav-links` element exists
- Ensure `initMobileMenu()` is called

**Styling issues?**
- Verify `/style.css` is loaded
- Check CSS custom properties
- Look for conflicting CSS rules

---

## Files to Know

- `/scripts/utils.js` - Breadcrumb & menu functions
- `/style.css` - Breadcrumb & menu styles
- `/index.html` - Main page with mobile menu
- `/bmi-calculator/index.html` - Example implementation
- `BREADCRUMB_AND_MOBILE_MENU_GUIDE.md` - Full guide
- `scripts/batch-add-breadcrumbs.mjs` - Batch update script

---

## Performance

- Breadcrumb: 0.5KB
- Mobile Menu: 0.3KB
- CSS: 1.2KB
- **Total: ~2KB** (negligible)

---

## Browser Support

✅ Chrome 90+  
✅ Firefox 88+  
✅ Safari 14+  
✅ Edge 90+  
✅ Mobile browsers

---

## Next Steps

1. ✅ Phase 1 Complete - Breadcrumbs & Mobile Menu
2. ⏳ Phase 2 - Batch update all tools
3. ⏳ Phase 3 - Fix game canvas sizing
4. ⏳ Phase 4 - Add missing functionality

---

**Need Help?** See `BREADCRUMB_AND_MOBILE_MENU_GUIDE.md`
